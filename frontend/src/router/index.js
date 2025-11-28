import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import ServerList from '../views/ServerList.vue'
import NetworkDeviceList from '../views/NetworkDeviceList.vue'
import ApplicationList from '../views/ApplicationList.vue'
import ServiceList from '../views/ServiceList.vue'
import DepartmentList from '../views/DepartmentList.vue'
import UserList from '../views/UserList.vue'
import ModelManagement from '../views/ModelManagement.vue'
import ServiceTemplate from '../views/ServiceTemplate.vue'
import ClusterTemplate from '../views/ClusterTemplate.vue'
import ServiceCategory from '../views/ServiceCategory.vue'
import HostAutoApply from '../views/HostAutoApply.vue'
import DynamicGroup from '../views/DynamicGroup.vue'
import CustomField from '../views/CustomField.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: { requiresAuth: false }
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: { requiresAuth: false }
  },
  {
    path: '/',
    name: 'dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/servers',
    name: 'servers',
    component: ServerList,
    meta: { requiresAuth: true }
  },
  {
    path: '/network-devices',
    name: 'network-devices',
    component: NetworkDeviceList,
    meta: { requiresAuth: true }
  },
  {
    path: '/applications',
    name: 'applications',
    component: ApplicationList,
    meta: { requiresAuth: true }
  },
  {
    path: '/services',
    name: 'services',
    component: ServiceList,
    meta: { requiresAuth: true }
  },
  {
    path: '/departments',
    name: 'departments',
    component: DepartmentList,
    meta: { requiresAuth: true }
  },
  {
    path: '/users',
    name: 'users',
    component: UserList,
    meta: { requiresAuth: true }
  },
  {
    path: '/model-management',
    name: 'model-management',
    component: ModelManagement,
    meta: { requiresAuth: true }
  },
  {
    path: '/service-template',
    name: 'service-template',
    component: ServiceTemplate,
    meta: { requiresAuth: true }
  },
  {
    path: '/cluster-template',
    name: 'cluster-template',
    component: ClusterTemplate,
    meta: { requiresAuth: true }
  },
  {
    path: '/service-category',
    name: 'service-category',
    component: ServiceCategory,
    meta: { requiresAuth: true }
  },
  {
    path: '/host-auto-apply',
    name: 'host-auto-apply',
    component: HostAutoApply,
    meta: { requiresAuth: true }
  },
  {
    path: '/dynamic-group',
    name: 'dynamic-group',
    component: DynamicGroup,
    meta: { requiresAuth: true }
  },
  {
    path: '/custom-field',
    name: 'custom-field',
    component: CustomField,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  // 检查是否需要登录
  if (to.meta.requiresAuth) {
    // 检查是否已登录
    const token = localStorage.getItem('token')
    if (token) {
      next()
    } else {
      next('/login')
    }
  } else {
    next()
  }
})

export default router