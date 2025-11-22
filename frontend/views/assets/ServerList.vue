<template>
  <div class="server-list-container">
    <el-card shadow="always">
      <template #header>
        <div class="card-header">
          <span>服务器列表</span>
          <el-button type="primary" @click="handleAddServer">
            <el-icon><Plus /></el-icon>
            添加服务器
          </el-button>
        </div>
      </template>
      
      <!-- 搜索和筛选 -->
      <div class="search-filter">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input
              v-model="searchQuery"
              placeholder="搜索服务器名称、IP或序列号"
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
              <el-option label="在线" value="online" />
              <el-option label="离线" value="offline" />
              <el-option label="维护中" value="maintenance" />
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
        :data="serversData"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" />
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="服务器名称" width="180" />
        <el-table-column prop="hostname" label="主机名" width="180" />
        <el-table-column prop="ip_address" label="IP地址" width="150" />
        <el-table-column prop="serial_number" label="序列号" width="200" />
        <el-table-column prop="server_type" label="服务器类型" width="120" />
        <el-table-column prop="os" label="操作系统" width="150" />
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
            <el-button type="primary" size="small" @click="handleEditServer(scope.row)">
              <el-icon><Edit /></el-icon>
              编辑
            </el-button>
            <el-button type="danger" size="small" @click="handleDeleteServer(scope.row)">
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
    
    <!-- 添加/编辑服务器对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="600px"
      @close="handleDialogClose"
    >
      <el-form
        ref="serverFormRef"
        :model="serverForm"
        :rules="formRules"
        label-width="120px"
      >
        <el-form-item label="服务器名称" prop="name">
          <el-input v-model="serverForm.name" placeholder="请输入服务器名称" />
        </el-form-item>
        <el-form-item label="主机名" prop="hostname">
          <el-input v-model="serverForm.hostname" placeholder="请输入主机名" />
        </el-form-item>
        <el-form-item label="IP地址" prop="ip_address">
          <el-input v-model="serverForm.ip_address" placeholder="请输入IP地址" />
        </el-form-item>
        <el-form-item label="序列号" prop="serial_number">
          <el-input v-model="serverForm.serial_number" placeholder="请输入序列号" />
        </el-form-item>
        <el-form-item label="服务器类型" prop="server_type">
          <el-select v-model="serverForm.server_type" placeholder="请选择服务器类型">
            <el-option label="物理机" value="physical" />
            <el-option label="虚拟机" value="virtual" />
            <el-option label="云主机" value="cloud" />
          </el-select>
        </el-form-item>
        <el-form-item label="操作系统" prop="os">
          <el-input v-model="serverForm.os" placeholder="请输入操作系统" />
        </el-form-item>
        <el-form-item label="所属部门" prop="department">
          <el-select v-model="serverForm.department" placeholder="请选择所属部门">
            <el-option
              v-for="dept in departments"
              :key="dept.id"
              :label="dept.name"
              :value="dept.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="状态" prop="status">
          <el-select v-model="serverForm.status" placeholder="请选择状态">
            <el-option label="在线" value="online" />
            <el-option label="离线" value="offline" />
            <el-option label="维护中" value="maintenance" />
          </el-select>
        </el-form-item>
        <el-form-item label="描述">
          <el-input
            v-model="serverForm.description"
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
  name: 'ServerList',
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
    const servers = ref([])
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
    const editingServer = ref(null)
    
    // 表单数据
    const serverForm = reactive({
      name: '',
      hostname: '',
      ip_address: '',
      serial_number: '',
      server_type: 'virtual',
      os: '',
      department: '',
      status: 'online',
      description: ''
    })
    
    // 表单验证规则
    const formRules = {
      name: [{ required: true, message: '请输入服务器名称', trigger: 'blur' }],
      hostname: [{ required: true, message: '请输入主机名', trigger: 'blur' }],
      ip_address: [{ required: true, message: '请输入IP地址', trigger: 'blur' }],
      serial_number: [{ required: true, message: '请输入序列号', trigger: 'blur' }],
      department: [{ required: true, message: '请选择所属部门', trigger: 'change' }]
    }
    
    // 计算属性：过滤后的数据
    const serversData = computed(() => {
      let filtered = [...servers.value]
      
      // 按搜索词筛选
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(server => 
          server.name?.toLowerCase().includes(query) ||
          server.ip_address?.includes(query) ||
          server.serial_number?.toLowerCase().includes(query) ||
          server.hostname?.toLowerCase().includes(query)
        )
      }
      
      // 按部门筛选
      if (selectedDepartment.value) {
        filtered = filtered.filter(server => 
          server.department === selectedDepartment.value
        )
      }
      
      // 按状态筛选
      if (selectedStatus.value) {
        filtered = filtered.filter(server => 
          server.status === selectedStatus.value
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
      return editingServer.value ? '编辑服务器' : '添加服务器'
    })
    
    // 加载服务器数据
    const loadServers = async () => {
      loading.value = true
      try {
        const response = await axios.get('/servers/')
        servers.value = response.data.results || []
      } catch (error) {
        console.error('加载服务器数据失败:', error)
        ElMessage.error('加载服务器数据失败')
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
    
    // 处理添加服务器
    const handleAddServer = () => {
      editingServer.value = null
      resetForm()
      dialogVisible.value = true
    }
    
    // 处理编辑服务器
    const handleEditServer = (server) => {
      editingServer.value = server
      // 填充表单数据
      Object.assign(serverForm, {
        name: server.name || '',
        hostname: server.hostname || '',
        ip_address: server.ip_address || '',
        serial_number: server.serial_number || '',
        server_type: server.server_type || 'virtual',
        os: server.os || '',
        department: server.department || '',
        status: server.status || 'online',
        description: server.description || ''
      })
      dialogVisible.value = true
    }
    
    // 重置表单
    const resetForm = () => {
      Object.assign(serverForm, {
        name: '',
        hostname: '',
        ip_address: '',
        serial_number: '',
        server_type: 'virtual',
        os: '',
        department: '',
        status: 'online',
        description: ''
      })
    }
    
    // 处理表单提交
    const handleSubmitForm = async () => {
      try {
        if (editingServer.value) {
          // 更新服务器
          await axios.put(`/servers/${editingServer.value.id}/`, serverForm)
          ElMessage.success('服务器更新成功')
        } else {
          // 添加服务器
          await axios.post('/servers/', serverForm)
          ElMessage.success('服务器添加成功')
        }
        dialogVisible.value = false
        loadServers() // 重新加载数据
      } catch (error) {
        console.error('提交表单失败:', error)
        ElMessage.error('操作失败，请重试')
      }
    }
    
    // 处理删除服务器
    const handleDeleteServer = (server) => {
      ElMessageBox.confirm(
        `确定要删除服务器「${server.name}」吗？`,
        '删除确认',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      ).then(async () => {
        try {
          await axios.delete(`/servers/${server.id}/`)
          ElMessage.success('删除成功')
          loadServers() // 重新加载数据
        } catch (error) {
          console.error('删除服务器失败:', error)
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
        case 'online': return 'success'
        case 'offline': return 'danger'
        case 'maintenance': return 'warning'
        default: return 'info'
      }
    }
    
    // 获取状态标签效果
    const getStatusTagEffect = (status) => {
      return status === 'online' ? 'dark' : 'plain'
    }
    
    // 获取状态文本
    const getStatusText = (status) => {
      switch (status) {
        case 'online': return '在线'
        case 'offline': return '离线'
        case 'maintenance': return '维护中'
        default: return status
      }
    }
    
    // 对话框关闭处理
    const handleDialogClose = () => {
      resetForm()
      editingServer.value = null
    }
    
    // 组件挂载时加载数据
    onMounted(() => {
      loadDepartments()
      loadServers()
    })
    
    return {
      loading,
      serversData,
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
      serverForm,
      formRules,
      handleAddServer,
      handleEditServer,
      handleDeleteServer,
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
.server-list-container {
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