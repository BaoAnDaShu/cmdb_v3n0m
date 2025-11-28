<template>
  <div>
    <!-- 登录和注册页面不显示头部和侧边栏 -->
    <div v-if="!isAuthPage" class="cmdb-app">
      <header class="app-header">
        <div class="header-left">
          <div class="logo">
            <i class="fas fa-cube"></i>
            <span>蓝鲸配置平台</span>
          </div>
          <nav class="header-nav">
            <router-link to="/" class="nav-item" :class="{ active: $route.path === '/' }">首页</router-link>
            <router-link to="/departments" class="nav-item" :class="{ active: $route.path === '/departments' }">业务</router-link>
            <router-link to="/servers" class="nav-item" :class="{ active: $route.path === '/servers' }">资源</router-link>
            <router-link to="/model-management" class="nav-item" :class="{ active: $route.path === '/model-management' }">模型</router-link>
            <router-link to="/services" class="nav-item" :class="{ active: $route.path === '/services' }">运营分析</router-link>
          </nav>
        </div>
        <div class="header-right">
          <div class="user-info">
            <span>admin</span>
            <i class="fas fa-chevron-down"></i>
          </div>
          <div class="help-icon">
            <i class="fas fa-question-circle"></i>
          </div>
        </div>
      </header>
      
      <div class="app-body">
        <nav class="sidebar">
          <ul class="menu">
            <li class="menu-item" :class="{ active: $route.name === 'dashboard' }" @click="$router.push('/')">
              <i class="fas fa-tachometer-alt"></i> 仪表盘
            </li>
            <li class="menu-item" :class="{ active: $route.name === 'servers' }" @click="$router.push('/servers')">
              <i class="fas fa-server"></i> 服务器列表
            </li>
            <li class="menu-item" :class="{ active: $route.name === 'network-devices' }" @click="$router.push('/network-devices')">
              <i class="fas fa-network-wired"></i> 网络设备
            </li>
            <li class="menu-item" :class="{ active: $route.name === 'applications' }" @click="$router.push('/applications')">
              <i class="fas fa-cubes"></i> 应用管理
            </li>
            <li class="menu-item" :class="{ active: $route.name === 'services' }" @click="$router.push('/services')">
              <i class="fas fa-cog"></i> 服务管理
            </li>
            <li class="menu-item" :class="{ active: $route.name === 'departments' }" @click="$router.push('/departments')">
              <i class="fas fa-sitemap"></i> 部门管理
            </li>
            <li class="menu-item" :class="{ active: $route.name === 'users' }" @click="$router.push('/users')">
              <i class="fas fa-users"></i> 用户管理
            </li>
          </ul>
        </nav>
        
        <main class="main-content">
          <router-view></router-view>
        </main>
      </div>
    </div>
    
    <!-- 登录和注册页面只显示router-view -->
    <div v-else>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isAuthPage() {
      // 判断当前页面是否是登录或注册页面
      return ['login', 'register'].includes(this.$route.name)
    }
  }
}
</script>

<style>
/* 全局样式重置 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', Arial, sans-serif;
  background-color: #f5f7fa;
  color: #303133;
}

/* 全局链接样式 */
a {
  color: #606266;
  text-decoration: none;
}

a:hover {
  color: #409eff;
  text-decoration: none;
}

/* 表格中的链接样式 */
.main-content table a {
  color: #606266;
}

.main-content table a:hover {
  color: #409eff;
}

/* 应用容器 */
.cmdb-app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* 头部样式 */
.app-header {
  background-color: #001529;
  color: white;
  padding: 0 20px;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  z-index: 1000;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 30px;
}

.logo {
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo i {
  font-size: 24px;
}

.header-nav {
  display: flex;
  gap: 0;
  background-color: transparent;
  border-radius: 0;
  overflow: visible;
}

.nav-item {
  color: #ffffff !important;
  text-decoration: none !important;
  padding: 20px 20px;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
  background-color: transparent;
  border-bottom: none;
}

.nav-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
  color: #ffffff !important;
}

.nav-item.active {
  background-color: rgba(255, 255, 255, 0.1);
  color: #ffffff !important;
  border-bottom: none;
  font-weight: 600;
}

/* 修复router-link的默认样式 */
.header-nav .router-link-active,
.header-nav .router-link-exact-active {
  background-color: rgba(255, 255, 255, 0.1);
  color: #ffffff !important;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-size: 14px;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.user-info:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.help-icon {
  cursor: pointer;
  font-size: 18px;
  padding: 5px;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.help-icon:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

/* 主体内容 */
.app-body {
  display: flex;
  flex: 1;
  min-height: 0;
}

/* 侧边栏样式 */
.sidebar {
  width: 240px;
  background-color: #304156;
  color: white;
  overflow-y: auto;
}

.menu {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu-item {
  padding: 15px 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: all 0.3s ease;
  border-left: 3px solid transparent;
}

.menu-item:hover {
  background-color: #263445;
  color: #ffffff;
}

.menu-item.active {
  background-color: #1989fa;
  color: #ffffff;
  border-left-color: #ffffff;
}

.menu-item i {
  font-size: 18px;
  width: 20px;
  text-align: center;
}

/* 主内容区域 */
.main-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  background-color: #f5f7fa;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    left: -240px;
    top: 60px;
    height: calc(100vh - 60px);
    z-index: 999;
    transition: left 0.3s ease;
  }
  
  .sidebar.show {
    left: 0;
  }
  
  .main-content {
    padding: 15px;
  }
}
</style>
