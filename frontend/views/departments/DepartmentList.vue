<template>
  <div class="department-list-container">
    <el-card shadow="always">
      <template #header>
        <div class="card-header">
          <span>部门管理</span>
          <el-button type="primary" @click="handleAddDepartment">
            <el-icon><Plus /></el-icon>
            添加部门
          </el-button>
        </div>
      </template>
      
      <!-- 搜索和筛选 -->
      <div class="search-filter">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input
              v-model="searchQuery"
              placeholder="搜索部门名称或描述"
              clearable
              @input="handleSearch"
              prefix-icon="el-icon-search"
            />
          </el-col>
          <el-col :span="6">
            <el-select
              v-model="selectedParent"
              placeholder="选择上级部门"
              clearable
              @change="handleFilter"
            >
              <el-option value="" label="无上级部门" />
              <el-option
                v-for="dept in departments"
                :key="dept.id"
                :label="dept.name"
                :value="dept.id"
              />
            </el-select>
          </el-col>
          <el-col :span="4">
            <el-button type="info" @click="resetFilters">
              <el-icon><Refresh /></el-icon>
              重置筛选
            </el-button>
          </el-col>
        </el-row>
      </div>
      
      <!-- 数据表格 -->
      <el-table
        v-loading="loading"
        :data="departmentsData"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" />
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="部门名称" width="180" />
        <el-table-column prop="code" label="部门代码" width="120" />
        <el-table-column label="上级部门" width="150">
          <template #default="scope">
            {{ getParentName(scope.row.parent) }}
          </template>
        </el-table-column>
        <el-table-column prop="manager" label="部门经理" width="120" />
        <el-table-column prop="phone" label="联系电话" width="120" />
        <el-table-column prop="email" label="邮箱" width="180" />
        <el-table-column prop="created_at" label="创建时间" width="180">
          <template #default="scope">
            {{ formatDate(scope.row.created_at) }}
          </template>
        </el-table-column>
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="scope">
            <el-button type="primary" size="small" @click="handleEditDepartment(scope.row)">
              <el-icon><Edit /></el-icon>
              编辑
            </el-button>
            <el-button type="danger" size="small" @click="handleDeleteDepartment(scope.row)">
              <el-icon><Delete /></el-icon>
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      
      <!-- 分页 -->
      <div class="pagination-container">
        <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :page-sizes="[10, 20, 50, 100]"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />
      </div>
    </el-card>
    
    <!-- 添加/编辑部门对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="600px"
      @close="handleDialogClose"
    >
      <el-form
        ref="departmentFormRef"
        :model="departmentForm"
        :rules="formRules"
        label-width="120px"
      >
        <el-form-item label="部门名称" prop="name">
          <el-input v-model="departmentForm.name" placeholder="请输入部门名称" />
        </el-form-item>
        <el-form-item label="部门代码" prop="code">
          <el-input v-model="departmentForm.code" placeholder="请输入部门代码" />
        </el-form-item>
        <el-form-item label="上级部门">
          <el-select v-model="departmentForm.parent" placeholder="请选择上级部门">
            <el-option value="" label="无上级部门" />
            <el-option
              v-for="dept in availableParentDepartments"
              :key="dept.id"
              :label="dept.name"
              :value="dept.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="部门经理" prop="manager">
          <el-input v-model="departmentForm.manager" placeholder="请输入部门经理姓名" />
        </el-form-item>
        <el-form-item label="联系电话">
          <el-input v-model="departmentForm.phone" placeholder="请输入联系电话" />
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="departmentForm.email" placeholder="请输入邮箱地址" />
        </el-form-item>
        <el-form-item label="描述">
          <el-input
            v-model="departmentForm.description"
            type="textarea"
            placeholder="请输入部门描述信息"
            :rows="3"
          />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="handleSubmitForm">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { ref, reactive, onMounted, computed } from 'vue'
import {
  Plus,
  Edit,
  Delete,
  Refresh,
  Search
} from '@element-plus/icons-vue'

export default {
  name: 'DepartmentList',
  components: {
    Plus,
    Edit,
    Delete,
    Refresh,
    Search
  },
  setup() {
    // 状态
    const loading = ref(false)
    const departments = ref([])
    const searchQuery = ref('')
    const selectedParent = ref('')
    const currentPage = ref(1)
    const pageSize = ref(10)
    const total = ref(0)
    const multipleSelection = ref([])
    
    // 对话框相关
    const dialogVisible = ref(false)
    const editingDepartment = ref(null)
    
    // 表单数据
    const departmentForm = reactive({
      name: '',
      code: '',
      parent: '',
      manager: '',
      phone: '',
      email: '',
      description: ''
    })
    
    // 表单验证规则
    const formRules = {
      name: [{ required: true, message: '请输入部门名称', trigger: 'blur' }],
      code: [{ required: true, message: '请输入部门代码', trigger: 'blur' }]
    }
    
    // 计算属性：过滤后的数据
    const departmentsData = computed(() => {
      let filtered = [...departments.value]
      
      // 按搜索词筛选
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(dept => 
          dept.name?.toLowerCase().includes(query) ||
          dept.code?.toLowerCase().includes(query) ||
          dept.description?.toLowerCase().includes(query)
        )
      }
      
      // 按上级部门筛选
      if (selectedParent.value !== '') {
        filtered = filtered.filter(dept => 
          dept.parent === (selectedParent.value === '' ? null : selectedParent.value)
        )
      }
      
      // 更新总数
      total.value = filtered.length
      
      // 分页
      const startIndex = (currentPage.value - 1) * pageSize.value
      const endIndex = startIndex + pageSize.value
      return filtered.slice(startIndex, endIndex)
    })
    
    // 可用的上级部门（排除正在编辑的部门自身）
    const availableParentDepartments = computed(() => {
      return departments.value.filter(dept => 
        !editingDepartment.value || dept.id !== editingDepartment.value.id
      )
    })
    
    // 获取对话框标题
    const dialogTitle = computed(() => {
      return editingDepartment.value ? '编辑部门' : '添加部门'
    })
    
    // 加载部门数据
    const loadDepartments = async () => {
      loading.value = true
      try {
        const response = await axios.get('/departments/')
        departments.value = response.data.results || []
      } catch (error) {
        console.error('加载部门数据失败:', error)
        ElMessage.error('加载部门数据失败')
      } finally {
        loading.value = false
      }
    }
    
    // 处理搜索
    const handleSearch = () => {
      currentPage.value = 1
    }
    
    // 处理筛选
    const handleFilter = () => {
      currentPage.value = 1
    }
    
    // 重置筛选条件
    const resetFilters = () => {
      searchQuery.value = ''
      selectedParent.value = ''
      currentPage.value = 1
    }
    
    // 处理添加部门
    const handleAddDepartment = () => {
      editingDepartment.value = null
      resetForm()
      dialogVisible.value = true
    }
    
    // 处理编辑部门
    const handleEditDepartment = (department) => {
      editingDepartment.value = department
      // 填充表单数据
      Object.assign(departmentForm, {
        name: department.name || '',
        code: department.code || '',
        parent: department.parent || '',
        manager: department.manager || '',
        phone: department.phone || '',
        email: department.email || '',
        description: department.description || ''
      })
      dialogVisible.value = true
    }
    
    // 重置表单
    const resetForm = () => {
      Object.assign(departmentForm, {
        name: '',
        code: '',
        parent: '',
        manager: '',
        phone: '',
        email: '',
        description: ''
      })
    }
    
    // 处理表单提交
    const handleSubmitForm = async () => {
      try {
        // 处理空值（将空字符串转换为null）
        const formData = { ...departmentForm }
        if (formData.parent === '') {
          formData.parent = null
        }
        
        if (editingDepartment.value) {
          // 更新部门
          await axios.put(`/departments/${editingDepartment.value.id}/`, formData)
          ElMessage.success('部门更新成功')
        } else {
          // 添加部门
          await axios.post('/departments/', formData)
          ElMessage.success('部门添加成功')
        }
        dialogVisible.value = false
        loadDepartments() // 重新加载数据
      } catch (error) {
        console.error('提交表单失败:', error)
        ElMessage.error('操作失败，请重试')
      }
    }
    
    // 处理删除部门
    const handleDeleteDepartment = (department) => {
      ElMessageBox.confirm(
        `确定要删除部门「${department.name}」吗？`,
        '删除确认',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      ).then(async () => {
        try {
          await axios.delete(`/departments/${department.id}/`)
          ElMessage.success('删除成功')
          loadDepartments() // 重新加载数据
        } catch (error) {
          console.error('删除部门失败:', error)
          ElMessage.error('删除失败，请重试')
        }
      }).catch(() => {
        // 取消删除
      })
    }
    
    // 处理选择变化
    const handleSelectionChange = (val) => {
      multipleSelection.value = val
    }
    
    // 分页处理
    const handleSizeChange = (size) => {
      pageSize.value = size
      currentPage.value = 1
    }
    
    const handleCurrentChange = (current) => {
      currentPage.value = current
    }
    
    // 格式化日期
    const formatDate = (dateString) => {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleString('zh-CN')
    }
    
    // 获取上级部门名称
    const getParentName = (parentId) => {
      if (!parentId) return '无'
      const parent = departments.value.find(d => d.id === parentId)
      return parent ? parent.name : '-'
    }
    
    // 对话框关闭处理
    const handleDialogClose = () => {
      resetForm()
      editingDepartment.value = null
    }
    
    // 组件挂载时加载数据
    onMounted(() => {
      loadDepartments()
    })
    
    return {
      loading,
      departmentsData,
      departments,
      availableParentDepartments,
      searchQuery,
      selectedParent,
      currentPage,
      pageSize,
      total,
      multipleSelection,
      dialogVisible,
      dialogTitle,
      departmentForm,
      formRules,
      handleAddDepartment,
      handleEditDepartment,
      handleDeleteDepartment,
      handleSubmitForm,
      handleSearch,
      handleFilter,
      resetFilters,
      handleSelectionChange,
      handleSizeChange,
      handleCurrentChange,
      formatDate,
      getParentName,
      handleDialogClose
    }
  }
}
</script>

<style scoped>
.department-list-container {
  padding: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.search-filter {
  margin-bottom: 20px;
  padding: 15px;
  background-color: #f5f7fa;
  border-radius: 4px;
}

.pagination-container {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
}
</style>