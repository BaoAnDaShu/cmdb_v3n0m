<template>
  <el-container class="app-container">
    <el-header class="app-header">
      <div class="header-content">
        <el-icon><HomeFilled /></el-icon>
        <h1 class="title">CMDB资产管理系统</h1>
      </div>
      <el-dropdown>
        <el-button type="primary" plain>
          <el-icon><Setting /></el-icon>
          系统设置
          <el-icon class="el-icon--right"><ArrowDown /></el-icon>
        </el-button>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="logout">
              <el-icon><SwitchButton /></el-icon>
              退出登录
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </el-header>
    
    <el-container>
      <el-aside width="240px" class="app-sidebar">
        <el-menu
          :default-active="activeMenu"
          class="el-menu-vertical"
          router
          @select="handleMenuSelect"
        >
          <el-menu-item index="/dashboard">
            <el-icon><DataAnalysis /></el-icon>
            <span>仪表盘</span>
          </el-menu-item>
          
          <el-sub-menu index="/assets">
            <template #title>
              <el-icon><Monitor /></el-icon>
              <span>资产管理</span>
            </template>
            <el-menu-item index="/assets/servers">服务器</el-menu-item>
            <el-menu-item index="/assets/network-devices">网络设备</el-menu-item>
          </el-sub-menu>
          
          <el-sub-menu index="/services">
            <template #title>
              <el-icon><Cpu /></el-icon>
              <span>服务管理</span>
            </template>
            <el-menu-item index="/services/applications">应用</el-menu-item>
            <el-menu-item index="/services/services">服务</el-menu-item>
          </el-sub-menu>
          
          <el-menu-item index="/departments">
            <el-icon><OfficeBuilding /></el-icon>
            <span>部门管理</span>
          </el-menu-item>
          
          <el-menu-item index="/relationships">
            <el-icon><Link /></el-icon>
            <span>关系管理</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      
      <el-main class="app-main">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import {
  HomeFilled,
  Setting,
  ArrowDown,
  SwitchButton,
  DataAnalysis,
  Monitor,
  Cpu,
  OfficeBuilding,
  Link
} from '@element-plus/icons-vue'

export default {
  name: 'App',
  components: {
    HomeFilled,
    Setting,
    ArrowDown,
    SwitchButton,
    DataAnalysis,
    Monitor,
    Cpu,
    OfficeBuilding,
    Link
  },
  setup() {
    const router = useRouter()
    const activeMenu = ref('')
    
    // 获取当前活动菜单
    const getActiveMenu = () => {
      const path = router.currentRoute.value.path
      // 如果是子菜单，返回父菜单ID
      if (path.includes('/assets/')) return '/assets'
      if (path.includes('/services/')) return '/services'
      return path || '/dashboard'
    }
    
    const handleMenuSelect = (key, keyPath) => {
      console.log('菜单选中:', key, keyPath)
    }
    
    const logout = () => {
      // 这里可以添加登出逻辑
      ElMessageBox.confirm('确定要退出登录吗？', '退出确认', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        ElMessage.success('已退出登录')
      })
    }
    
    onMounted(() => {
      activeMenu.value = getActiveMenu()
      
      // 监听路由变化，更新活动菜单
      router.beforeEach((to, from, next) => {
        activeMenu.value = getActiveMenu()
        next()
      })
    })
    
    return {
      activeMenu,
      handleMenuSelect,
      logout
    }
  }
}
</script>

<style scoped>
.app-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  background-color: #1989fa;
  color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-content {
  display: flex;
  align-items: center;
  gap: 10px;
}

.title {
  margin: 0;
  font-size: 20px;
  font-weight: 500;
}

.app-sidebar {
  background-color: #f5f7fa;
  box-shadow: 2px 0 6px rgba(0, 21, 41, 0.1);
}

.app-main {
  padding: 20px;
  background-color: #f5f7fa;
  overflow-y: auto;
}

.el-menu-vertical {
  height: 100%;
  border-right: none;
}

/* 过渡动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>