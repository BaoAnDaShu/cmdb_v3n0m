<template>
  <div class="server-list-container">
    <h2>服务器列表</h2>
    <div class="server-list">
      <div v-if="loading" class="loading">
        加载中...
      </div>
      <div v-else-if="servers.length === 0" class="empty">
        没有服务器数据
      </div>
      <div v-else class="server-grid">
        <div v-for="server in servers" :key="server.id" class="server-card">
          <div class="server-header">
            <h3>{{ server.name }}</h3>
            <span class="status-badge" :class="server.status">
              {{ getStatusLabel(server.status) }}
            </span>
          </div>
          <div class="server-info">
            <p><strong>主机名:</strong> {{ server.hostname }}</p>
            <p><strong>IP地址:</strong> {{ server.ip_address }}</p>
            <p><strong>操作系统:</strong> {{ server.os_type }} {{ server.os_version }}</p>
            <p><strong>CPU:</strong> {{ server.cpu }}</p>
            <p><strong>内存:</strong> {{ server.memory }}</p>
            <p><strong>磁盘:</strong> {{ server.disk }}</p>
            <p><strong>所属部门:</strong> {{ server.department_name }}</p>
            <p><strong>管理员:</strong> {{ server.administrator }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ServerList',
  data() {
    return {
      servers: [],
      loading: true
    }
  },
  mounted() {
    this.fetchServers()
  },
  methods: {
    fetchServers() {
      this.loading = true
      this.$axios.get('/servers/')
        .then(response => {
          this.servers = response.data.results || response.data
          this.loading = false
        })
        .catch(error => {
          console.error('获取服务器数据失败:', error)
          this.loading = false
        })
    },
    getStatusLabel(status) {
      const statusMap = {
        'running': '运行中',
        'stopped': '已停止',
        'maintenance': '维护中',
        'fault': '故障'
      }
      return statusMap[status] || status
    }
  }
}
</script>

<style scoped>
.server-list-container {
  padding: 20px;
}

.loading, .empty {
  text-align: center;
  padding: 40px;
  color: #909399;
}

.server-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.server-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.server-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
}

.server-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.server-header h3 {
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

.status-badge.fault {
  background-color: #fff1f0;
  color: #ff4d4f;
  border: 1px solid #ffccc7;
}

.server-info p {
  margin: 8px 0;
  color: #606266;
  font-size: 14px;
}

.server-info strong {
  color: #303133;
}
</style>