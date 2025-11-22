<template>
  <div class="network-device-list-container">
    <el-card shadow="always">
      <template #header>
        <div class="card-header">
          <span>网络设备列表</span>
          <el-button type="primary" @click="handleAddDevice">
            <el-icon><Plus /></el-icon>
            添加网络设备
          </el-button>
        </div>
      </template>
      
      <!-- 搜索和筛选 -->
      <div class="search-filter">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input
              v-model="searchQuery"
              placeholder="搜索设备名称、IP或序列号"
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
              v-model="selectedType"
              placeholder="选择设备类型"
              clearable
              @change="handleFilter"
            >
              <el-option label="交换机" value="switch" />
              <el-option label="路由器" value="router" />
              <el-option label="防火墙" value="firewall" />
              <el-option label="负载均衡" value="load_balancer" />
              <el-option label="其他" value="other" />
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
        :data="networkDevicesData"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" />
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="设备名称" width="180" />
        <el-table-column prop="ip_address" label="IP地址" width="150" />
        <el-table-column prop="serial_number" label="序列号" width="200" />
        <el-table-column prop="device_type" label="设备类型" width="120">
          <template #default="scope">
            {{ getDeviceTypeText(scope.row.device_type) }}
          </template>
        </el-table-column>
        <el-table-column prop="model" label="设备型号" width="150" />
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
            <el-button type="primary" size="small" @click="handleEditDevice(scope.row)">
              <el-icon><Edit /></el-icon>
              编辑
            </el-button>
            <el-button type="danger" size="small" @click="handleDeleteDevice(scope.row)">
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
    
    <!-- 添加/编辑网络设备对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="600px"
      @close="handleDialogClose"
    >
      <el-form
        ref="deviceFormRef"
        :model="deviceForm"
        :rules="formRules"
        label-width="120px"
      >
        <el-form-item label="设备名称" prop="name">
          <el-input v-model="deviceForm.name" placeholder="请输入设备名称" />
        </el-form-item>
        <el-form-item label="IP地址" prop="ip_address">
          <el-input v-model="deviceForm.ip_address" placeholder="请输入IP地址" />
        </el-form-item>
        <el-form-item label="序列号" prop="serial_number">
          <el-input v-model="deviceForm.serial_number" placeholder="请输入序列号" />
        </el-form-item>
        <el-form-item label="设备类型" prop="device_type">
          <el-select v-model="deviceForm.device_type" placeholder="请选择设备类型">
            <el-option label="交换机" value="switch" />
            <el-option label="路由器" value="router" />
            <el-option label="防火墙" value="firewall" />
            <el-option label="负载均衡" value="load_balancer" />
            <el-option label="其他" value="other" />
          </el-select>
        </el-form-item>
        <el-form-item label="设备型号" prop="model">
          <el-input v-model="deviceForm.model" placeholder="请输入设备型号" />
        </el-form-item>
        <el-form-item label="所属部门" prop="department">
          <el-select v-model="deviceForm.department" placeholder="请选择所属部门">
            <el-option
              v-for="dept in departments"
              :key="dept.id"
              :label="dept.name"
              :value="dept.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="状态" prop="status">
          <el-select v-model="deviceForm.status" placeholder="请选择状态">
            <el-option label="在线" value="online" />
            <el-option label="离线" value="offline" />
            <el-option label="维护中" value="maintenance" />
          </el-select>
        </el-form-item>
        <el-form-item label="描述">
          <el-input
            v-model="deviceForm.description"
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
  name: 'NetworkDeviceList',
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
    const networkDevices = ref([])
    const departments = ref([])
    const searchQuery = ref('')
    const selectedDepartment = ref('')
    const selectedType = ref('')
    const currentPage = ref(1)
    const pageSize = ref(10)
    const total = ref(0)
    const multipleSelection = ref([])
    
    // 对话框相关
    const dialogVisible = ref(false)
    const editingDevice = ref(null)
    
    // 表单数据
    const deviceForm = reactive({
      name: '',
      ip_address: '',
      serial_number: '',
      device_type: 'switch',
      model: '',
      department: '',
      status: 'online',
      description: ''
    })
    
    // 表单验证规则
    const formRules = {
      name: [{ required: true, message: '请输入设备名称', trigger: 'blur' }],
      ip_address: [{ required: true, message: '请输入IP地址', trigger: 'blur' }],
      serial_number: [{ required: true, message: '请输入序列号', trigger: 'blur' }],
      device_type: [{ required: true, message: '请选择设备类型', trigger: 'change' }],
      department: [{ required: true, message: '请选择所属部门', trigger: 'change' }]
    }
    
    // 计算属性：过滤后的数据
    const networkDevicesData = computed(() => {
      let filtered = [...networkDevices.value]
      
      // 按搜索词筛选
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(device => 
          device.name?.toLowerCase().includes(query) ||
          device.ip_address?.includes(query) ||
          device.serial_number?.toLowerCase().includes(query)
        )
      }
      
      // 按部门筛选
      if (selectedDepartment.value) {
        filtered = filtered.filter(device => 
          device.department === selectedDepartment.value
        )
      }
      
      // 按设备类型筛选
      if (selectedType.value) {
        filtered = filtered.filter(device => 
          device.device_type === selectedType.value
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
      return editingDevice.value ? '编辑网络设备' : '添加网络设备'
    })
    
    // 加载网络设备数据
    const loadNetworkDevices = async () => {
      loading.value = true
      try {
        const response = await axios.get('/network-devices/')
        networkDevices.value = response.data.results || []
      } catch (error) {
        console.error('加载网络设备数据失败:', error)
        ElMessage.error('加载网络设备数据失败')
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
      selectedType.value = ''
      currentPage.value = 1
    }
    
    // 处理添加设备
    const handleAddDevice = () => {
      editingDevice.value = null
      resetForm()
      dialogVisible.value = true
    }
    
    // 处理编辑设备
    const handleEditDevice = (device) => {
      editingDevice.value = device
      // 填充表单数据
      Object.assign(deviceForm, {
        name: device.name || '',
        ip_address: device.ip_address || '',
        serial_number: device.serial_number || '',
        device_type: device.device_type || 'switch',
        model: device.model || '',
        department: device.department || '',
        status: device.status || 'online',
        description: device.description || ''
      })
      dialogVisible.value = true
    }
    
    // 重置表单
    const resetForm = () => {
      Object.assign(deviceForm, {
        name: '',
        ip_address: '',
        serial_number: '',
        device_type: 'switch',
        model: '',
        department: '',
        status: 'online',
        description: ''
      })
    }
    
    // 处理表单提交
    const handleSubmitForm = async () => {
      try {
        if (editingDevice.value) {
          // 更新设备
          await axios.put(`/network-devices/${editingDevice.value.id}/`, deviceForm)
          ElMessage.success('网络设备更新成功')
        } else {
          // 添加设备
          await axios.post('/network-devices/', deviceForm)
          ElMessage.success('网络设备添加成功')
        }
        dialogVisible.value = false
        loadNetworkDevices() // 重新加载数据
      } catch (error) {
        console.error('提交表单失败:', error)
        ElMessage.error('操作失败，请重试')
      }
    }
    
    // 处理删除设备
    const handleDeleteDevice = (device) => {
      ElMessageBox.confirm(
        `确定要删除网络设备「${device.name}」吗？`,
        '删除确认',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      ).then(async () => {
        try {
          await axios.delete(`/network-devices/${device.id}/`)
          ElMessage.success('删除成功')
          loadNetworkDevices() // 重新加载数据
        } catch (error) {
          console.error('删除网络设备失败:', error)
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
    
    // 获取设备类型文本
    const getDeviceTypeText = (type) => {
      const typeMap = {
        'switch': '交换机',
        'router': '路由器',
        'firewall': '防火墙',
        'load_balancer': '负载均衡',
        'other': '其他'
      }
      return typeMap[type] || type
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
      editingDevice.value = null
    }
    
    // 组件挂载时加载数据
    onMounted(() => {
      loadDepartments()
      loadNetworkDevices()
    })
    
    return {
      loading,
      networkDevicesData,
      departments,
      searchQuery,
      selectedDepartment,
      selectedType,
      currentPage,
      pageSize,
      total,
      multipleSelection,
      dialogVisible,
      dialogTitle,
      deviceForm,
      formRules,
      handleAddDevice,
      handleEditDevice,
      handleDeleteDevice,
      handleSubmitForm,
      handleSearch,
      handleFilter,
      resetFilters,
      handleSelectionChange,
      handleSizeChange,
      handleCurrentChange,
      formatDate,
      getDepartmentName,
      getDeviceTypeText,
      getStatusTagType,
      getStatusTagEffect,
      getStatusText,
      handleDialogClose
    }
  }
}
</script>

<style scoped>
.network-device-list-container {
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