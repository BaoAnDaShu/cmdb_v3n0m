<template>
  <div class="network-device-list-container">
    <h2>网络设备列表</h2>
    <div class="network-device-list">
      <div v-if="loading" class="loading">
        加载中...
      </div>
      <div v-else-if="devices.length === 0" class="empty">
        没有网络设备数据
      </div>
      <div v-else class="device-grid">
        <div v-for="device in devices" :key="device.id" class="device-card">
          <div class="device-header">
            <h3>{{ device.name }}</h3>
            <span class="device-type-badge">
              {{ getDeviceTypeLabel(device.device_type) }}
            </span>
          </div>
          <div class="device-info">
            <p><strong>管理IP:</strong> {{ device.ip_address }}</p>
            <p><strong>厂商:</strong> {{ device.vendor }}</p>
            <p><strong>型号:</strong> {{ device.model }}</p>
            <p><strong>序列号:</strong> {{ device.serial_number || '未提供' }}</p>
            <p><strong>所属部门:</strong> {{ device.department_name }}</p>
            <p><strong>物理位置:</strong> {{ device.location }}</p>
            <p><strong>管理员:</strong> {{ device.administrator }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NetworkDeviceList',
  data() {
    return {
      devices: [],
      loading: true
    }
  },
  mounted() {
    this.fetchDevices()
  },
  methods: {
    fetchDevices() {
      this.loading = true
      this.$axios.get('/network-devices/')
        .then(response => {
          this.devices = response.data.results || response.data
          this.loading = false
        })
        .catch(error => {
          console.error('获取网络设备数据失败:', error)
          this.loading = false
        })
    },
    getDeviceTypeLabel(type) {
      const typeMap = {
        'switch': '交换机',
        'router': '路由器',
        'firewall': '防火墙',
        'loadbalancer': '负载均衡器',
        'other': '其他'
      }
      return typeMap[type] || type
    }
  }
}
</script>

<style scoped>
.network-device-list-container {
  padding: 20px;
}

.loading, .empty {
  text-align: center;
  padding: 40px;
  color: #909399;
}

.device-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.device-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.device-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
}

.device-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.device-header h3 {
  margin: 0;
  color: #303133;
  font-size: 18px;
}

.device-type-badge {
  padding: 4px 8px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: 500;
  background-color: #e6f7ff;
  color: #1890ff;
  border: 1px solid #91d5ff;
}

.device-info p {
  margin: 8px 0;
  color: #606266;
  font-size: 14px;
}

.device-info strong {
  color: #303133;
}
</style>