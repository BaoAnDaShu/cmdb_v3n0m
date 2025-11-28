import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

// 配置Axios
app.config.globalProperties.$axios = axios
axios.defaults.baseURL = 'http://localhost:8000/api'
axios.defaults.headers.common['Content-Type'] = 'application/json'

// 添加请求拦截器，自动添加token
axios.interceptors.request.use(
  config => {
    // 从localStorage获取token
    const token = localStorage.getItem('token')
    // 如果token存在，添加到请求头
    if (token) {
      config.headers.Authorization = `Token ${token}`
    } else {
      // 如果token不存在，移除Authorization头
      delete config.headers.Authorization
    }
    return config
  },
  error => {
    // 处理请求错误
    return Promise.reject(error)
  }
)

// 添加响应拦截器，处理token无效的情况
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    // 处理401错误，清除无效token并跳转到登录页
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      // 跳转到登录页
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

// 使用插件
app.use(router)
app.use(ElementPlus)

app.mount('#app')
