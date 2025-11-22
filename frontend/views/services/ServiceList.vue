<template>
  <div class="service-list-container">
    <el-card shadow="always">
      <template #header>
        <div class="card-header">
          <span>服务列表</span>
          <el-button type="primary" @click="handleAddService">
            <el-icon><Plus /></el-icon>
            添加服务
          </el-button>
        </div>
      </template>
      
      <!-- 搜索和筛选 -->
      <div class="search-filter">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input
              v-model="searchQuery"
              placeholder="搜索服务名称或描述"
              clearable
              @input="handleSearch"
              prefix-icon="el-icon-search"
            />
          </el-col>
          <el-col :span="6">
            <el-select
              v-model="selectedApplication"
              placeholder="选择所属应用"
              clearable
              @change="handleFilter"
            >
              <el-option
                v-for="app in applications"
                :key="app.id"
                :label="app.name"
                :value="app.id"
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
              <el-option label="异常" value="error" />
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
        :data="servicesData"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" />
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="服务名称" width="180" />
        <el-table-column prop="service_type" label="服务类型" width="120" />
        <el-table-column prop="version" label="版本" width="100" />
        <el-table-column label="所属应用" width="150">
          <template #default="scope">
            {{ getApplicationName(scope.row.application) }}
          </template>
        </el-table-column>
        <el-table-column label="运行服务器" width="150">
          <template #default="scope">
            {{ getServerName(scope.row.server) }}
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
            <el-button type="primary" size="small" @click="handleEditService(scope.row)">
              <el-icon><Edit /></el-icon>
              编辑
            </el-button>
            <el-button type="danger" size="small" @click="handleDeleteService(scope.row)">
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
    
    <!-- 添加/编辑服务对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="600px"
      @close="handleDialogClose"
    >
      <el-form
        ref="serviceFormRef"
        :model="serviceForm"
        :rules="formRules"
        label-width="120px"
      >
        <el-form-item label="服务名称" prop="name">
          <el-input v-model="serviceForm.name" placeholder="请输入服务名称" />
        </el-form-item>
        <el-form-item label="服务类型" prop="service_type">
          <el-input v-model="serviceForm.service_type" placeholder="请输入服务类型" />
        </el-form-item>
        <el-form-item label="版本" prop="version">
          <el-input v-model="serviceForm.version" placeholder="请输入版本号" />
        </el-form-item>
        <el-form-item label="所属应用" prop="application">
          <el-select v-model="serviceForm.application" placeholder="请选择所属应用">
            <el-option
              v-for="app in applications"
              :key="app.id"
              :label="app.name"
              :value="app.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="运行服务器" prop="server">
          <el-select v-model="serviceForm.server" placeholder="请选择运行服务器">
            <el-option
              v-for="server in servers"
              :key="server.id"
              :label="server.name"
              :value="server.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="状态" prop="status">
          <el-select v-model="serviceForm.status" placeholder="请选择状态">
            <el-option label="运行中" value="running" />
            <el-option label="已停止" value="stopped" />
            <el-option label="异常" value="error" />
          </el-select>
        </el-form-item>
        <el-form-item label="描述">
          <el-input
            v-model="serviceForm.description"
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
  name: 'ServiceList',
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
    const services = ref([])
    const applications = ref([])
    const servers = ref([])
    const searchQuery = ref('')
    const selectedApplication = ref('')
    const selectedStatus = ref('')
    const currentPage = ref(1)
    const pageSize = ref(10)
    const total = ref(0)
    const multipleSelection = ref([])
    
    // 对话框相关
    const dialogVisible = ref(false)
    const editingService = ref(null)
    
    // 表单数据
    const serviceForm = reactive({
      name: '',
      service_type: '',
      version: '',
      application: '',
      server: '',
      status: 'running',
      description: ''
    })
    
    // 表单验证规则
    const formRules = {
      name: [{ required: true, message: '请输入服务名称', trigger: 'blur' }],
      application: [{ required: true, message: '请选择所属应用', trigger: 'change' }],
      server: [{ required: true, message: '请选择运行服务器', trigger: 'change' }]
    }
    
    // 计算属性：过滤后的数据
    const servicesData = computed(() => {
      let filtered = [...services.value]
      
      // 按搜索词筛选
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(service => 
          service.name?.toLowerCase().includes(query) ||
          service.description?.toLowerCase().includes(query)
        )
      }
      
      // 按应用筛选
      if (selectedApplication.value) {
        filtered = filtered.filter(service => 
          service.application === selectedApplication.value
        )
      }
      
      // 按状态筛选
      if (selectedStatus.value) {
        filtered = filtered.filter(service => 
          service.status === selectedStatus.value
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
      return editingService.value ? '编辑服务' : '添加服务'
    })
    
    // 加载服务数据
    const loadServices = async () => {
      loading.value = true
      try {
        const response = await axios.get('/services/')
        services.value = response.data.results || []
      } catch (error) {
        console.error('加载服务数据失败:', error)
        ElMessage.error('加载服务数据失败')
      } finally {
        loading.value = false
      }
    }
    
    // 加载应用数据
    const loadApplications = async () => {
      try {
        const response = await axios.get('/applications/')
        applications.value = response.data.results || []
      } catch (error) {
        console.error('加载应用数据失败:', error)
        ElMessage.error('加载应用数据失败')
      }
    }
    
    // 加载服务器数据
    const loadServers = async () => {
      try {
        const response = await axios.get('/servers/')
        servers.value = response.data.results || []
      } catch (error) {
        console.error('加载服务器数据失败:', error)
        ElMessage.error('加载服务器数据失败')
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
      selectedApplication.value = ''
      selectedStatus.value = ''
      currentPage.value = 1
    }
    
    // 处理添加服务
    const handleAddService = () => {
      editingService.value = null
      resetForm()
      dialogVisible.value = true
    }
    
    // 处理编辑服务
    const handleEditService = (service) => {
      editingService.value = service
      // 填充表单数据
      Object.assign(serviceForm, {
        name: service.name || '',
        service_type: service.service_type || '',
        version: service.version || '',
        application: service.application || '',
        server: service.server || '',
        status: service.status || 'running',
        description: service.description || ''
      })
      dialogVisible.value = true
    }
    
    // 重置表单
    const resetForm = () => {
      Object.assign(serviceForm, {
        name: '',
        service_type: '',
        version: '',
        application: '',
        server: '',
        status: 'running',
        description: ''
      })
    }
    
    // 处理表单提交
    const handleSubmitForm = async () => {
      try {
        if (editingService.value) {
          // 更新服务
          await axios.put(`/services/${editingService.value.id}/`, serviceForm)
          ElMessage.success('服务更新成功')
        } else {
          // 添加服务
          await axios.post('/services/', serviceForm)
          ElMessage.success('服务添加成功')
        }
        dialogVisible.value = false
        loadServices() // 重新加载数据
      } catch (error) {
        console.error('提交表单失败:', error)
        ElMessage.error('操作失败，请重试')
      }
    }
    
    // 处理删除服务
    const handleDeleteService = (service) => {
      ElMessageBox.confirm(
        `确定要删除服务「${service.name}」吗？`,
        '删除确认',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      ).then(async () => {
        try {
          await axios.delete(`/services/${service.id}/`)
          ElMessage.success('删除成功')
          loadServices() // 重新加载数据
        } catch (error) {
          console.error('删除服务失败:', error)
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
    
    // 获取应用名称
    const getApplicationName = (applicationId) => {
      const app = applications.value.find(a => a.id === applicationId)
      return app ? app.name : '-'
    }
    
    // 获取服务器名称
    const getServerName = (serverId) => {
      const server = servers.value.find(s => s.id === serverId)
      return server ? server.name : '-'
    }
    
    // 获取状态标签类型
    const getStatusTagType = (status) => {
      switch (status) {
        case 'running': return 'success'
        case 'stopped': return 'danger'
        case 'error': return 'warning'
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
        case 'error': return '异常'
        default: return status
      }
    }
    
    // 对话框关闭处理
    const handleDialogClose = () => {
      resetForm()
      editingService.value = null
    }
    
    // 组件挂载时加载数据
    onMounted(() => {
      loadApplications()
      loadServers()
      loadServices()
    })
    
    return {
      loading,
      servicesData,
      applications,
      servers,
      searchQuery,
      selectedApplication,
      selectedStatus,
      currentPage,
      pageSize,
      total,
      multipleSelection,
      dialogVisible,
      dialogTitle,
      serviceForm,
      formRules,
      handleAddService,
      handleEditService,
      handleDeleteService,
      handleSubmitForm,
      handleSearch,
      handleFilter,
      resetFilters,
      handleSelectionChange,
      handleSizeChange,
      handleCurrentChange,
      formatDate,
      getApplicationName,
      getServerName,
      getStatusTagType,
      getStatusTagEffect,
      getStatusText,
      handleDialogClose
    }
  }
}
</script>

<style scoped>
.service-list-container {
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