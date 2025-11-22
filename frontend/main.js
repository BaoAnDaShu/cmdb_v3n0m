// Vue应用入口文件 - 完全基于CDN版本

// 创建Vue应用实例
const app = Vue.createApp({
    template: `
        <div class="cmdb-app">
            <header class="app-header">
                <h1>CMDB资产管理系统</h1>
                <div class="user-info">
                    <span>管理员</span>
                </div>
            </header>
            
            <div class="app-body">
                <nav class="sidebar">
                    <ul class="menu">
                        <li class="menu-item" :class="{ active: currentPage === 'dashboard' }" @click="changePage('dashboard')">
                            <i class="fas fa-tachometer-alt"></i> 仪表盘
                        </li>
                        <li class="menu-item" :class="{ active: currentPage === 'servers' }" @click="changePage('servers')">
                            <i class="fas fa-server"></i> 服务器列表
                        </li>
                        <li class="menu-item" :class="{ active: currentPage === 'network' }" @click="changePage('network')">
                            <i class="fas fa-network-wired"></i> 网络设备
                        </li>
                        <li class="menu-item" :class="{ active: currentPage === 'applications' }" @click="changePage('applications')">
                            <i class="fas fa-cubes"></i> 应用管理
                        </li>
                        <li class="menu-item" :class="{ active: currentPage === 'services' }" @click="changePage('services')">
                            <i class="fas fa-cog"></i> 服务管理
                        </li>
                        <li class="menu-item" :class="{ active: currentPage === 'departments' }" @click="changePage('departments')">
                            <i class="fas fa-sitemap"></i> 部门管理
                        </li>
                        <li class="menu-item" :class="{ active: currentPage === 'users' }" @click="changePage('users')">
                            <i class="fas fa-users"></i> 用户管理
                        </li>
                    </ul>
                </nav>
                
                <main class="main-content">
                    <div v-if="currentPage === 'dashboard'">
                        <h2>系统概览</h2>
                        <p>欢迎使用CMDB资产管理系统</p>
                        <button class="test-btn" @click="testAPI">测试API连接</button>
                        <div v-if="apiResult" class="api-result">
                            <h3>API测试结果</h3>
                            <pre>{{ apiResult }}</pre>
                        </div>
                    </div>
                    <div v-else>
                        <h2>{{ pageTitle }}</h2>
                        <p>正在加载 {{ pageTitle }} 功能...</p>
                    </div>
                </main>
            </div>
        </div>
    `,
    
    data() {
        return {
            currentPage: 'dashboard',
            apiResult: null
        }
    },
    
    computed: {
        pageTitle() {
            const titles = {
                'dashboard': '仪表盘',
                'servers': '服务器列表',
                'network': '网络设备',
                'applications': '应用管理',
                'services': '服务管理',
                'departments': '部门管理',
                'users': '用户管理'
            }
            return titles[this.currentPage] || '页面未找到'
        }
    },
    
    methods: {
        changePage(page) {
            this.currentPage = page
        },
        
        testAPI() {
            // 测试API连接
            axios.get('http://localhost:8000/api/departments/')
                .then(response => {
                    this.apiResult = JSON.stringify(response.data, null, 2)
                    alert('API连接成功!')
                })
                .catch(error => {
                    this.apiResult = '错误: ' + error.message
                    alert('API连接失败: ' + error.message)
                })
        }
    }
})

// 挂载应用
app.mount('#app')