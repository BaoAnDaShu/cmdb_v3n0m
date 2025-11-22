<template>
  <div class="dashboard-container">
    <el-card shadow="always" class="dashboard-card">
      <template #header>
        <div class="card-header">
          <span>系统概览</span>
          <el-button type="text" size="small">
            <el-icon><Refresh /></el-icon>
            刷新数据
          </el-button>
        </div>
      </template>
      
      <!-- 统计卡片 -->
      <el-row :gutter="20" class="stats-row">
        <el-col :span="6">
          <el-card class="stat-card" :body-style="{ padding: '20px' }">
            <div class="stat-content">
              <div class="stat-icon server-icon">
                <el-icon><Server /></el-icon>
              </div>
              <div class="stat-info">
                <p class="stat-number">{{ serverCount }}</p>
                <p class="stat-label">服务器总数</p>
              </div>
            </div>
          </el-card>
        </el-col>
        
        <el-col :span="6">
          <el-card class="stat-card" :body-style="{ padding: '20px' }">
            <div class="stat-content">
              <div class="stat-icon network-icon">
                <el-icon><Wifi /></el-icon>
              </div>
              <div class="stat-info">
                <p class="stat-number">{{ networkCount }}</p>
                <p class="stat-label">网络设备</p>
              </div>
            </div>
          </el-card>
        </el-col>
        
        <el-col :span="6">
          <el-card class="stat-card" :body-style="{ padding: '20px' }">
            <div class="stat-content">
              <div class="stat-icon app-icon">
                <el-icon><App /></el-icon>
              </div>
              <div class="stat-info">
                <p class="stat-number">{{ applicationCount }}</p>
                <p class="stat-label">应用数量</p>
              </div>
            </div>
          </el-card>
        </el-col>
        
        <el-col :span="6">
          <el-card class="stat-card" :body-style="{ padding: '20px' }">
            <div class="stat-content">
              <div class="stat-icon dept-icon">
                <el-icon><OfficeBuilding /></el-icon>
              </div>
              <div class="stat-info">
                <p class="stat-number">{{ departmentCount }}</p>
                <p class="stat-label">部门数量</p>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
      
      <!-- 图表区域 -->
      <el-row :gutter="20" class="charts-row">
        <el-col :span="12">
          <el-card class="chart-card">
            <template #header>
              <div class="chart-header">
                <span>资产分布</span>
              </div>
            </template>
            <div class="chart-container">
              <div id="assetDistributionChart" class="chart"></div>
            </div>
          </el-card>
        </el-col>
        
        <el-col :span="12">
          <el-card class="chart-card">
            <template #header>
              <div class="chart-header">
                <span>近期操作记录</span>
              </div>
            </template>
            <div class="recent-operations">
              <el-timeline>
                <el-timeline-item
                  v-for="(item, index) in recentOperations"
                  :key="index"
                  :timestamp="item.time"
                  :type="item.type"
                  :color="item.color"
                  :icon="item.icon"
                >
                  <div class="timeline-content">
                    <p class="operation-title">{{ item.title }}</p>
                    <p class="operation-detail">{{ item.detail }}</p>
                  </div>
                </el-timeline-item>
              </el-timeline>
            </div>
          </el-card>
        </el-col>
      </el-row>
      
      <!-- 快速操作 -->
      <el-card class="quick-actions-card">
        <template #header>
          <div class="card-header">
            <span>快速操作</span>
          </div>
        </template>
        <div class="quick-actions">
          <el-button type="primary" @click="navigateTo('/assets/servers')">
            <el-icon><Plus /></el-icon>
            添加服务器
          </el-button>
          <el-button type="success" @click="navigateTo('/assets/network-devices')">
            <el-icon><Plus /></el-icon>
            添加网络设备
          </el-button>
          <el-button type="info" @click="navigateTo('/departments')">
            <el-icon><Plus /></el-icon>
            添加部门
          </el-button>
          <el-button type="warning" @click="navigateTo('/services/applications')">
            <el-icon><Plus /></el-icon>
            添加应用
          </el-button>
        </div>
      </el-card>
    </el-card>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import {
  Refresh,
  Server,
  Wifi,
  App,
  OfficeBuilding,
  Plus
} from '@element-plus/icons-vue'

export default {
  name: 'Dashboard',
  components: {
    Refresh,
    Server,
    Wifi,
    App,
    OfficeBuilding,
    Plus
  },
  setup() {
    const router = useRouter()
    
    // 统计数据
    const serverCount = ref(0)
    const networkCount = ref(0)
    const applicationCount = ref(0)
    const departmentCount = ref(0)
    
    // 近期操作记录
    const recentOperations = ref([
      {
        time: '10分钟前',
        title: '新增服务器',
        detail: '添加了服务器：web-server-01',
        type: 'primary',
        color: '#1989fa',
        icon: 'Plus'
      },
      {
        time: '30分钟前',
        title: '更新网络设备',
        detail: '更新了网络设备：switch-main-01',
        type: 'success',
        color: '#67c23a',
        icon: 'Edit'
      },
      {
        time: '1小时前',
        title: '创建部门',
        detail: '创建了新部门：研发部',
        type: 'info',
        color: '#409eff',
        icon: 'OfficeBuilding'
      },
      {
        time: '3小时前',
        title: '添加应用',
        detail: '添加了应用：用户管理系统',
        type: 'warning',
        color: '#e6a23c',
        icon: 'App'
      }
    ])
    
    // 导航到指定页面
    const navigateTo = (path) => {
      router.push(path)
    }
    
    // 加载数据
    const loadData = async () => {
      try {
        // 获取服务器数量
        const serversResponse = await axios.get('/servers/')
        serverCount.value = serversResponse.data.count || 0
        
        // 获取网络设备数量
        const networksResponse = await axios.get('/network-devices/')
        networkCount.value = networksResponse.data.count || 0
        
        // 获取应用数量
        const appsResponse = await axios.get('/applications/')
        applicationCount.value = appsResponse.data.count || 0
        
        // 获取部门数量
        const deptsResponse = await axios.get('/departments/')
        departmentCount.value = deptsResponse.data.count || 0
        
        // 初始化图表
        await nextTick()
        initAssetDistributionChart()
      } catch (error) {
        console.error('加载仪表盘数据失败:', error)
        ElMessage.error('数据加载失败，请稍后重试')
      }
    }
    
    // 初始化资产分布图表
    const initAssetDistributionChart = () => {
      // 这里可以使用 Chart.js 或其他图表库
      console.log('图表初始化')
      // 模拟图表渲染
      const chartElement = document.getElementById('assetDistributionChart')
      if (chartElement) {
        chartElement.innerHTML = `
          <div style="text-align: center; padding: 40px;">
            <el-icon :size="48" style="color: #909399;"><DataLine /></el-icon>
            <p style="margin-top: 10px; color: #909399;">图表区域</p>
          </div>
        `
      }
    }
    
    // 组件挂载时加载数据
    onMounted(() => {
      loadData()
    })
    
    return {
      serverCount,
      networkCount,
      applicationCount,
      departmentCount,
      recentOperations,
      navigateTo
    }
  }
}
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
}

.dashboard-card {
  margin-bottom: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.stats-row {
  margin-bottom: 20px;
}

.stat-card {
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.stat-content {
  display: flex;
  align-items: center;
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 20px;
  font-size: 24px;
}

.server-icon {
  background-color: #e6f7ff;
  color: #1890ff;
}

.network-icon {
  background-color: #f6ffed;
  color: #52c41a;
}

.app-icon {
  background-color: #fff7e6;
  color: #fa8c16;
}

.dept-icon {
  background-color: #f9f0ff;
  color: #722ed1;
}

.stat-info {
  flex: 1;
}

.stat-number {
  margin: 0;
  font-size: 32px;
  font-weight: 600;
  color: #333;
}

.stat-label {
  margin: 5px 0 0 0;
  font-size: 14px;
  color: #999;
}

.charts-row {
  margin-bottom: 20px;
}

.chart-card {
  height: 400px;
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chart-container {
  height: calc(100% - 50px);
  padding: 10px;
}

.chart {
  width: 100%;
  height: 100%;
}

.recent-operations {
  max-height: 350px;
  overflow-y: auto;
}

.timeline-content {
  padding: 0;
}

.operation-title {
  margin: 0 0 5px 0;
  font-weight: 500;
  color: #333;
}

.operation-detail {
  margin: 0;
  font-size: 12px;
  color: #999;
}

.quick-actions-card {
  margin-top: 20px;
}

.quick-actions {
  display: flex;
  gap: 15px;
}
</style>