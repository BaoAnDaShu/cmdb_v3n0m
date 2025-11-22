// 路由配置文件
import { createRouter, createWebHistory } from 'vue-router'

// 导入页面组件（使用懒加载）
const Dashboard = () => import('../views/Dashboard.vue')
const ServerList = () => import('../views/assets/ServerList.vue')
const NetworkDeviceList = () => import('../views/assets/NetworkDeviceList.vue')
const ApplicationList = () => import('../views/services/ApplicationList.vue')
const ServiceList = () => import('../views/services/ServiceList.vue')
const DepartmentList = () => import('../views/DepartmentList.vue')
const RelationshipList = () => import('../views/RelationshipList.vue')

// 路由配置
const routes = [
  {
    path: '/',
    redirect: '/dashboard'
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      title: '仪表盘',
      requiresAuth: false
    }
  },
  {
    path: '/assets/servers',
    name: 'ServerList',
    component: ServerList,
    meta: {
      title: '服务器列表',
      requiresAuth: false
    }
  },
  {
    path: '/assets/network-devices',
    name: 'NetworkDeviceList',
    component: NetworkDeviceList,
    meta: {
      title: '网络设备列表',
      requiresAuth: false
    }
  },
  {
    path: '/services/applications',
    name: 'ApplicationList',
    component: ApplicationList,
    meta: {
      title: '应用列表',
      requiresAuth: false
    }
  },
  {
    path: '/services/services',
    name: 'ServiceList',
    component: ServiceList,
    meta: {
      title: '服务列表',
      requiresAuth: false
    }
  },
  {
    path: '/departments',
    name: 'DepartmentList',
    component: DepartmentList,
    meta: {
      title: '部门列表',
      requiresAuth: false
    }
  },
  {
    path: '/relationships',
    name: 'RelationshipList',
    component: RelationshipList,
    meta: {
      title: '关系列表',
      requiresAuth: false
    }
  },
  // 404页面
  {
    path: '/:pathMatch(.*)*',
    redirect: '/dashboard'
  }
]

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由前置守卫
router.beforeEach((to, from, next) => {
  // 设置页面标题
  document.title = `${to.meta.title || 'CMDB系统'} - CMDB资产管理系统`
  
  // 这里可以添加认证逻辑
  // if (to.meta.requiresAuth && !isAuthenticated) {
  //   next('/login')
  // } else {
  //   next()
  // }
  
  next()
})

export default router