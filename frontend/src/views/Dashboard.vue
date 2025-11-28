<template>
  <div class="dashboard-container">
    <div class="dashboard-header">
      <h2>系统概览</h2>
      <div class="welcome-message">
        <p>欢迎回来，{{ username }}！</p>
        <span class="current-time">{{ currentTime }}</span>
      </div>
    </div>
    
    <!-- 数据统计卡片 -->
    <div class="stats-cards">
      <div class="stat-card" v-for="stat in stats" :key="stat.id">
        <div class="stat-header">
          <h3>{{ stat.title }}</h3>
          <i :class="stat.icon" class="stat-icon"></i>
        </div>
        <div class="stat-content">
          <div class="stat-value">{{ stat.value }}</div>
          <div class="stat-change" :class="stat.changeType">
            <i :class="stat.changeIcon"></i> {{ stat.change }}%
          </div>
        </div>
        <div class="stat-description">{{ stat.description }}</div>
      </div>
    </div>
    
    <!-- 资源分布图表 -->
    <div class="charts-section">
      <div class="chart-card">
        <h3>资源分布</h3>
        <div class="chart-placeholder">
          <div class="chart-item" v-for="item in resourceDistribution" :key="item.type">
            <div class="chart-item-header">
              <span class="chart-item-type">{{ item.type }}</span>
              <span class="chart-item-count">{{ item.count }}</span>
            </div>
            <div class="chart-item-bar">
              <div class="chart-item-progress" :style="{ width: item.percentage + '%' }" :class="item.color"></div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 最近活动 -->
      <div class="activity-card">
        <h3>最近活动</h3>
        <div class="activity-list">
          <div class="activity-item" v-for="activity in recentActivities" :key="activity.id">
            <div class="activity-icon" :class="activity.type"></div>
            <div class="activity-content">
              <div class="activity-title">{{ activity.title }}</div>
              <div class="activity-time">{{ activity.time }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 快速操作 -->
    <div class="quick-actions">
      <h3>快速操作</h3>
      <div class="action-buttons">
        <el-button type="primary" @click="addServer" icon="Plus" round>
          添加服务器
        </el-button>
        <el-button type="success" @click="addNetworkDevice" icon="Plus" round>
          添加网络设备
        </el-button>
        <el-button type="info" @click="addApplication" icon="Plus" round>
          添加应用
        </el-button>
        <el-button type="warning" @click="addService" icon="Plus" round>
          添加服务
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      username: '管理员',
      currentTime: '',
      stats: [
        {
          id: 1,
          title: '服务器总数',
          value: 128,
          change: 12.5,
          changeType: 'increase',
          changeIcon: 'el-icon-arrow-up',
          icon: 'el-icon-server',
          description: '较上月增长12.5%'
        },
        {
          id: 2,
          title: '网络设备',
          value: 64,
          change: 8.3,
          changeType: 'increase',
          changeIcon: 'el-icon-arrow-up',
          icon: 'el-icon-s-grid',
          description: '较上月增长8.3%'
        },
        {
          id: 3,
          title: '应用数量',
          value: 32,
          change: 5.0,
          changeType: 'increase',
          changeIcon: 'el-icon-arrow-up',
          icon: 'el-icon-apps',
          description: '较上月增长5.0%'
        },
        {
          id: 4,
          title: '服务数量',
          value: 48,
          change: -2.1,
          changeType: 'decrease',
          changeIcon: 'el-icon-arrow-down',
          icon: 'el-icon-service',
          description: '较上月减少2.1%'
        }
      ],
      resourceDistribution: [
        { type: '服务器', count: 128, percentage: 50, color: 'blue' },
        { type: '网络设备', count: 64, percentage: 25, color: 'green' },
        { type: '应用', count: 32, percentage: 12.5, color: 'yellow' },
        { type: '服务', count: 48, percentage: 12.5, color: 'red' }
      ],
      recentActivities: [
        { id: 1, title: '添加了新服务器', type: 'add', time: '2025-11-29 10:30' },
        { id: 2, title: '更新了网络设备信息', type: 'update', time: '2025-11-29 09:15' },
        { id: 3, title: '删除了过期应用', type: 'delete', time: '2025-11-28 16:45' },
        { id: 4, title: '添加了新服务', type: 'add', time: '2025-11-28 14:20' },
        { id: 5, title: '更新了部门信息', type: 'update', time: '2025-11-28 11:05' }
      ]
    }
  },
  mounted() {
    this.updateCurrentTime()
    setInterval(this.updateCurrentTime, 1000)
    this.fetchUsername()
  },
  methods: {
    updateCurrentTime() {
      const now = new Date()
      this.currentTime = now.toLocaleString('zh-CN')
    },
    fetchUsername() {
      // 从localStorage获取用户名
      const user = localStorage.getItem('user')
      if (user) {
        try {
          const userData = JSON.parse(user)
          this.username = userData.username || '管理员'
        } catch (error) {
          console.error('解析用户数据失败:', error)
        }
      }
    },
    addServer() {
      this.$message.info('添加服务器功能开发中')
    },
    addNetworkDevice() {
      this.$message.info('添加网络设备功能开发中')
    },
    addApplication() {
      this.$message.info('添加应用功能开发中')
    },
    addService() {
      this.$message.info('添加服务功能开发中')
    }
  }
}
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100%;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.dashboard-header h2 {
  font-size: 24px;
  font-weight: 600;
  color: #303133;
  margin: 0;
}

.welcome-message {
  text-align: right;
}

.welcome-message p {
  margin: 0;
  font-size: 16px;
  font-weight: 500;
  color: #606266;
}

.current-time {
  font-size: 14px;
  color: #909399;
}

/* 统计卡片样式 */
.stats-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-bottom: 24px;
}

.stat-card {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px 0 rgba(0, 0, 0, 0.15);
}

.stat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.stat-header h3 {
  font-size: 16px;
  font-weight: 500;
  color: #606266;
  margin: 0;
}

.stat-icon {
  font-size: 24px;
  color: #1989fa;
}

.stat-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.stat-value {
  font-size: 32px;
  font-weight: 600;
  color: #303133;
}

.stat-change {
  font-size: 14px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
}

.stat-change.increase {
  color: #52c41a;
}

.stat-change.decrease {
  color: #ff4d4f;
}

.stat-description {
  font-size: 14px;
  color: #909399;
}

/* 图表区域 */
.charts-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 24px;
}

.chart-card, .activity-card {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.chart-card h3, .activity-card h3 {
  font-size: 18px;
  font-weight: 600;
  color: #303133;
  margin: 0 0 20px 0;
}

.chart-placeholder {
  padding: 10px 0;
}

.chart-item {
  margin-bottom: 20px;
}

.chart-item:last-child {
  margin-bottom: 0;
}

.chart-item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.chart-item-type {
  font-size: 14px;
  color: #606266;
}

.chart-item-count {
  font-size: 14px;
  font-weight: 500;
  color: #303133;
}

.chart-item-bar {
  height: 8px;
  background-color: #f0f2f5;
  border-radius: 4px;
  overflow: hidden;
}

.chart-item-progress {
  height: 100%;
  border-radius: 4px;
  transition: width 0.3s ease;
}

.chart-item-progress.blue {
  background-color: #1989fa;
}

.chart-item-progress.green {
  background-color: #52c41a;
}

.chart-item-progress.yellow {
  background-color: #faad14;
}

.chart-item-progress.red {
  background-color: #ff4d4f;
}

/* 最近活动 */
.activity-list {
  max-height: 300px;
  overflow-y: auto;
}

.activity-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid #f0f2f5;
}

.activity-item:last-child {
  border-bottom: none;
}

.activity-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 16px;
  flex-shrink: 0;
}

.activity-icon.add {
  background-color: #52c41a;
}

.activity-icon.update {
  background-color: #1989fa;
}

.activity-icon.delete {
  background-color: #ff4d4f;
}

.activity-content {
  flex: 1;
}

.activity-title {
  font-size: 14px;
  color: #303133;
  margin-bottom: 4px;
}

.activity-time {
  font-size: 12px;
  color: #909399;
}

/* 快速操作 */
.quick-actions {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.quick-actions h3 {
  font-size: 18px;
  font-weight: 600;
  color: #303133;
  margin: 0 0 20px 0;
}

.action-buttons {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .charts-section {
    grid-template-columns: 1fr;
  }
  
  .stats-cards {
    grid-template-columns: 1fr;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .action-buttons .el-button {
    width: 100%;
  }
}
</style>