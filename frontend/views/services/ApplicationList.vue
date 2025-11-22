<template>
  <div class="application-list-container">
    <el-card shadow="always">
      <template #header>
        <div class="card-header">
          <span>应用列表</span>
          <el-button type="primary" @click="handleAddApplication">
            <el-icon><Plus /></el-icon>
            添加应用
          </el-button>
        </div>
      </template>
      
      <!-- 搜索和筛选 -->
      <div class="search-filter">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input
              v-model="searchQuery"
              placeholder="搜索应用名称或描述"
              clearable
              @input="handleSearch"
              prefix-icon="el-icon-search"
            />
          </el-col>
          <el-col :span="6">
            <el-select
              v-model="selectedDepartment"
              placeholder="选择所属部门"
              clearable
              @change="handleFilter"
            >
              <el-option
                v-for="dept in departments"
                :key="dept.id"
                :label="dept.name"
                :value="dept.id"
              />
            </el-select>
          </el-col>
          <el-col :span="6">
            <el-select
              v-model="selectedStatus"
              placeholder="选择状态"
              clearable
              @change="handleFilter"
            >
              <el-option label="运行中" value="running" />
              <el-option label="已停止" value="stopped" />
              <el-option label="开发中" value="developing" />
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
        :data="applicationsData"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" />
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="应用名称" width="200" />
        <el-table-column prop="code" label="应用编码" width="150" />
        <el-table-column prop="version" label="版本" width="100" />
        <el-table-column prop="app_type" label="应用类型" width="120" />
        <el-table-column label="所属部门" width="120">
          <template #default="scope">
            {{ getDepartmentName(scope.row.department) }}
          </template>
        </el-table-column>
        <el-table-column prop="status" label="状态" width="100">
          <template #default="scope">
            <el-tag
              :type="getStatusTagType(scope.row.status)"
              :effect="getStatusTagEffect(scope.row.status)"
            >
              {{ getStatusText(scope.row.status) }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="created_at" label="创建时间" width="180">
          <template #default="scope">
            {{ formatDate(scope.row.created_at) }}
          </template>
        </el-table-column>
        <el-table-column label="操作" width="150" fixed="right">
          <template #default="scope">
            <el-button type="primary" size="small" @click="handleEditApplication(scope.row)">
              <el-icon><Edit /></el-icon>
              编辑
            </el-button>
            <el-button type="danger" size="small" @click="handleDeleteApplication(scope.row)">
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
    
    <!-- 添加/编辑应用对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="600px"
      @close="handleDialogClose"
    >
      <el-form
        ref="applicationFormRef"
        :model="applicationForm"
        :rules="formRules"
        label-width="120px"
      >
        <el-form-item label="应用名称" prop="name">
          <el-input v-model="applicationForm.name" placeholder="请输入应用名称" />
        </el-form-item>
        <el-form-item label="应用编码" prop="code">
          <el-input v-model="applicationForm.code" placeholder="请输入应用编码" />
        </el-form-item>
        <el-form-item label="版本" prop="version">
          <el-input v-model="applicationForm.version" placeholder="请输入版本号" />
        </el-form-item>
        <el-form-item label="应用类型" prop="app_type">
          <el-input v-model="applicationForm.app_type" placeholder="请输入应用类型" />
        </el-form-item>
        <el-form-item label="所属部门" prop="department">
          <el-select v-model="applicationForm.department" placeholder="请选择所属部门">
            <el-option
              v-for="dept in departments"
              :key="dept.id"
              :label="dept.name"
              :value="dept.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="状态" prop="status">
          <el-select v-model="applicationForm.status" placeholder="请选择状态">
            <el-option label="运行中" value="running" />
            <el-option label="已停止" value="stopped" />
            <el-option label="开发中" value="developing" />
          </el-select>
        </el-form-item>
        <el-form-item label="描述">
          <el-input
            v-model="applicationForm.description"
            type="textarea"
            placeholder="请输入描述信息"
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
  name: 'ApplicationList',
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
    const applications = ref([])
    const departments = ref([])
    const searchQuery = ref('')
    const selectedDepartment = ref('')
    const selectedStatus = ref('')
    const currentPage = ref(1)
    const pageSize = ref(10)
    const total = ref(0)
    const multipleSelection = ref([])
    
    // 对话框相关
    const dialogVisible = ref(false)
    const editingApplication = ref(null)
    
    // 表单数据
    const applicationForm = reactive({
      name: '',
      code: '',
      version: '',
      app_type: '',
      department: '',
      status: 'running',
      description: ''
    })
    
    // 表单验证规则
    const formRules = {
      name: [{ required: true, message: '请输入应用名称', trigger: 'blur' }],
      code: [{ required: true, message: '请输入应用编码', trigger: 'blur' }],
      department: [{ required: true, message: '请选择所属部门', trigger: 'change' }]
    }
    
    // 计算属性：过滤后的数据
    const applicationsData = computed(() => {
      let filtered = [...applications.value]
      
      // 按搜索词筛选
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(app => 
          app.name?.toLowerCase().includes(query) ||
          app.description?.toLowerCase().includes(query) ||
          app.code?.toLowerCase().includes(query)
        )
      }
      
      // 按部门筛选
      if (selectedDepartment.value) {
        filtered = filtered.filter(app => 
          app.department === selectedDepartment.value
        )
      }
      
      // 按状态筛选
      if (selectedStatus.value) {
        filtered = filtered.filter(app => 
          app.status === selectedStatus.value
        )
      }
      
      // 更新总数
      total.value = filtered.length
      
      // 分页
      const startIndex = (currentPage.value - 1) * pageSize.value
      const endIndex = startIndex + pageSize.value
      return filtered.slice(startIndex, endIndex)
    })
    
    // 获取对话框标题
    const dialogTitle = computed(() => {
      return editingApplication.value ? '编辑应用' : '添加应用'
    })
    
    // 加载应用数据
    const loadApplications = async () => {
      loading.value = true
      try {
        const response = await axios.get('/applications/')
        applications.value = response.data.results || []
      } catch (error) {
        console.error('加载应用数据失败:', error)
        ElMessage.error('加载应用数据失败')
      } finally {
        loading.value = false
      }
    }
    
    // 加载部门数据
    const loadDepartments = async () => {
      try {
        const response = await axios.get('/departments/')
        departments.value = response.data.results || []
      } catch (error) {
        console.error('加载部门数据失败:', error)
        ElMessage.error('加载部门数据失败')
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
      selectedDepartment.value = ''
      selectedStatus.value = ''
      currentPage.value = 1
    }
    
    // 处理添加应用
    const handleAddApplication = () => {
      editingApplication.value = null
      resetForm()
      dialogVisible.value = true
    }
    
    // 处理编辑应用
    const handleEditApplication = (application) => {
      editingApplication.value = application
      // 填充表单数据
      Object.assign(applicationForm, {
        name: application.name || '',
        code: application.code || '',
        version: application.version || '',
        app_type: application.app_type || '',
        department: application.department || '',
        status: application.status || 'running',
        description: application.description || ''
      })
      dialogVisible.value = true
    }
    
    // 重置表单
    const resetForm = () => {
      Object.assign(applicationForm, {
        name: '',
        code: '',
        version: '',
        app_type: '',
        department: '',
        status: 'running',
        description: ''
      })
    }
    
    // 处理表单提交
    const handleSubmitForm = async () => {
      try {
        if (editingApplication.value) {
          // 更新应用
          await axios.put(`/applications/${editingApplication.value.id}/`, applicationForm)
          ElMessage.success('应用更新成功')
        } else {
          // 添加应用
          await axios.post('/applications/', applicationForm)
          ElMessage.success('应用添加成功')
        }
        dialogVisible.value = false
        loadApplications() // 重新加载数据
      } catch (error) {
        console.error('提交表单失败:', error)
        ElMessage.error('操作失败，请重试')
      }
    }
    
    // 处理删除应用
    const handleDeleteApplication = (application) => {
      ElMessageBox.confirm(
        `确定要删除应用「${application.name}」吗？`,
        '删除确认',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      ).then(async () => {
        try {
          await axios.delete(`/applications/${application.id}/`)
          ElMessage.success('删除成功')
          loadApplications() // 重新加载数据
        } catch (error) {
          console.error('删除应用失败:', error)
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
    
    // 获取部门名称
    const getDepartmentName = (departmentId) => {
      const dept = departments.value.find(d => d.id === departmentId)
      return dept ? dept.name : '-'
    }
    
    // 获取状态标签类型
    const getStatusTagType = (status) => {
      switch (status) {
        case 'running': return 'success'
        case 'stopped': return 'danger'
        case 'developing': return 'warning'
        default: return 'info'
      }
    }
    
    // 获取状态标签效果
    const getStatusTagEffect = (status) => {
      return status === 'running' ? 'dark' : 'plain'
    }
    
    // 获取状态文本
    const getStatusText = (status) => {
      switch (status) {
        case 'running': return '运行中'
        case 'stopped': return '已停止'
        case 'developing': return '开发中'
        default: return status
      }
    }
    
    // 对话框关闭处理
    const handleDialogClose = () => {
      resetForm()
      editingApplication.value = null
    }
    
    // 组件挂载时加载数据
    onMounted(() => {
      loadDepartments()
      loadApplications()
    })
    
    return {
      loading,
      applicationsData,
      departments,
      searchQuery,
      selectedDepartment,
      selectedStatus,
      currentPage,
      pageSize,
      total,
      multipleSelection,
      dialogVisible,
      dialogTitle,
      applicationForm,
      formRules,
      handleAddApplication,
      handleEditApplication,
      handleDeleteApplication,
      handleSubmitForm,
      handleSearch,
      handleFilter,
      resetFilters,
      handleSelectionChange,
      handleSizeChange,
      handleCurrentChange,
      formatDate,
      getDepartmentName,
      getStatusTagType,
      getStatusTagEffect,
      getStatusText,
      handleDialogClose
    }
  }
}
</script>

<style scoped>
.application-list-container {
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