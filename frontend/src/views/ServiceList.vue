<template>
  <div class="service-list-container">
    <h2>服务列表</h2>
    <div class="service-list">
      <div v-if="loading" class="loading">
        加载中...
      </div>
      <div v-else-if="services.length === 0" class="empty">
        没有服务数据
      </div>
      <div v-else class="service-grid">
        <div v-for="service in services" :key="service.id" class="service-card">
          <div class="service-header">
            <h3>{{ service.name }}</h3>
            <span class="status-badge" :class="service.status">
              {{ getStatusLabel(service.status) }}
            </span>
          </div>
          <div class="service-info">
            <p><strong>所属应用:</strong> {{ service.application_name }}</p>
            <p><strong>部署服务器:</strong> {{ service.server_name }} ({{ service.server_ip }})</p>
            <p v-if="service.port"><strong>服务端口:</strong> {{ service.port }}</p>
            <p v-if="service.description" class="description"><strong>描述:</strong> {{ service.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ServiceList',
  data() {
    return {
      services: [],
      loading: true
    }
  },
  mounted() {
    this.fetchServices()
  },
  methods: {
    fetchServices() {
      this.loading = true
      this.$axios.get('/services/')
        .then(response => {
          this.services = response.data.results || response.data
          this.loading = false
        })
        .catch(error => {
          console.error('获取服务数据失败:', error)
          this.loading = false
        })
    },
    getStatusLabel(status) {
      const statusMap = {
        'running': '运行中',
        'stopped': '已停止',
        'maintenance': '维护中',
        'deploying': '部署中'
      }
      return statusMap[status] || status
    }
  }
}
</script>

<style scoped>
.service-list-container {
  padding: 20px;
}

.loading, .empty {
  text-align: center;
  padding: 40px;
  color: #909399;
}

.service-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.service-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
}

.service-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.service-header h3 {
  margin: 0;
  color: #303133;
  font-size: 18px;
}

.status-badge {
  padding: 4px 8px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: 500;
}

.status-badge.running {
  background-color: #f6ffed;
  color: #52c41a;
  border: 1px solid #b7eb8f;
}

.status-badge.stopped {
  background-color: #fff2f0;
  color: #ff4d4f;
  border: 1px solid #ffccc7;
}

.status-badge.maintenance {
  background-color: #fff7e6;
  color: #fa8c16;
  border: 1px solid #ffe7ba;
}

.status-badge.deploying {
  background-color: #f0f5ff;
  color: #1890ff;
  border: 1px solid #adc6ff;
}

.service-info p {
  margin: 8px 0;
  color: #606266;
  font-size: 14px;
}

.service-info .description {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.service-info strong {
  color: #303133;
}
</style>