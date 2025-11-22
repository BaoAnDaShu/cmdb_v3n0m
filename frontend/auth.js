// 插入通用CSS样式重置，解决文字错位问题
(function() {
    const style = document.createElement('style');
    style.textContent = `
        /* 字体渲染优化 */
        * {
            box-sizing: border-box;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-rendering: optimizeLegibility;
            font-family: 'Microsoft YaHei', 'PingFang SC', 'Hiragino Sans GB', 'Heiti SC', Arial, sans-serif;
        }
        
        /* 解决文字错位问题 */
        html, body {
            font-size: 14px;
            line-height: 1.5;
            letter-spacing: 0;
            color: #303133;
        }
        
        /* 确保容器正常显示 */
        #app {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 30px 20px;
        }
        
        /* 修复卡片布局 */
        .test-card {
            margin-bottom: 25px !important;
            background-color: white !important;
            border-radius: 8px !important;
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1) !important;
        }
        
        /* 修复按钮样式 */
        .el-button {
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-family: inherit;
            height: 32px;
            padding: 0 15px;
        }
        
        /* 修复图标和文字对齐 - Element Plus 2.x 兼容 */
        .el-button .el-icon,
        .section-title .el-icon {
            margin-right: 8px !important;
            vertical-align: middle;
            font-size: 16px;
        }
        
        /* 修复Element Plus 2.x 图标显示 */
        .el-icon {
            vertical-align: middle;
            margin-right: 4px;
            font-size: 1em;
            display: inline-block;
        }
        
        /* 确保按钮组正常布局 */
        .btn-group {
            display: flex !important;
            flex-wrap: wrap !important;
            gap: 10px !important;
            margin-bottom: 15px;
        }
        
        /* 修复认证状态区域布局 */
        .auth-status {
            display: flex !important;
            align-items: center !important;
            gap: 10px !important;
            margin-bottom: 15px;
        }
        
        /* 修复标签和按钮的对齐 */
        .el-tag {
            display: inline-flex !important;
            align-items: center !important;
            vertical-align: middle !important;
        }
        
        /* 修复选择器样式 */
        .el-select {
            width: 100%;
        }
        
        /* 修复表单标签 */
        .form-item label {
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
            color: #606266;
        }
        
        /* 修复标题样式 */
        .section-title {
            font-size: 16px;
            font-weight: 600;
            color: #303133;
            margin-bottom: 15px;
            display: flex !important;
            align-items: center !important;
        }
        
        /* 修复API测试表单 */
        .api-test-form {
            margin-bottom: 15px;
        }
        
        /* 修复用户信息区域 */
        .user-info {
            padding: 12px;
            background-color: #f5f7fa;
            border-radius: 6px;
            margin-top: 10px;
            font-size: 13px;
        }
        
        /* 修复测试结果区域 */
        .test-result {
            margin-top: 15px;
            padding: 12px;
            border-radius: 4px;
            background-color: #f4f4f5;
            border-left: 4px solid #909399;
            max-height: 250px;
            overflow-y: auto;
            font-family: monospace;
            white-space: pre-wrap;
            font-size: 13px;
        }
        
        /* 防止选择器嵌套错误 */
        .el-select .el-option {
            display: block !important;
        }
        
        /* 确保el-icon正确渲染 */
        :deep(.el-icon) {
            font-family: inherit;
        }
    `;
    document.head.appendChild(style);
})();

// 用户认证相关的API调用工具
const BASE_URL = 'http://localhost:8000/api';

// 用户认证类
class AuthService {
    // 登录方法
    async login(username, password) {
        try {
            const response = await axios.post(`${BASE_URL}/login/`, {
                username,
                password
            });
            
            // 保存token和用户信息到localStorage
            if (response.data.token) {
                localStorage.setItem('token', response.data.token);
                localStorage.setItem('user', JSON.stringify(response.data.user));
            }
            
            return response.data;
        } catch (error) {
            // 处理错误情况
            if (error.response) {
                throw new Error(error.response.data.detail || '登录失败');
            } else if (error.request) {
                throw new Error('网络错误，请检查连接');
            } else {
                throw new Error('登录请求失败');
            }
        }
    }
    
    // 注册方法
    async register(username, email, password) {
        try {
            const response = await axios.post(`${BASE_URL}/register/`, {
                username,
                email,
                password
            });
            return response.data;
        } catch (error) {
            // 处理错误情况
            if (error.response) {
                throw new Error(error.response.data.detail || '注册失败');
            } else if (error.request) {
                throw new Error('网络错误，请检查连接');
            } else {
                throw new Error('注册请求失败');
            }
        }
    }
    
    // 登出方法
    logout() {
        // 清除localStorage中的token和用户信息
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        // 重定向到登录页面
        window.location.href = '/login.html';
    }
    
    // 获取当前用户信息
    getCurrentUser() {
        const userStr = localStorage.getItem('user');
        if (userStr) {
            return JSON.parse(userStr);
        }
        return null;
    }
    
    // 获取认证token
    getToken() {
        return localStorage.getItem('token');
    }
    
    // 检查用户是否已认证
    isAuthenticated() {
        return !!localStorage.getItem('token');
    }
    
    // 获取用户权限
    getUserPermissions() {
        const user = this.getCurrentUser();
        return user ? user.permissions || [] : [];
    }
    
    // 检查用户是否有指定权限
    hasPermission(permission) {
        const permissions = this.getUserPermissions();
        return permissions.includes(permission);
    }
    
    // 检查用户是否为管理员
    isAdmin() {
        const user = this.getCurrentUser();
        return user && (user.role === 'admin' || user.is_staff);
    }
}

// 创建单例实例并挂载到window对象
const authService = new AuthService();
window.authService = authService;

// 设置Axios请求拦截器函数
function setupAuthInterceptor() {
    axios.interceptors.request.use(
        (config) => {
            const token = authService.getToken();
            if (token) {
                config.headers['Authorization'] = `Token ${token}`;
            }
            return config;
        },
        (error) => {
            return Promise.reject(error);
        }
    );
    
    // 添加响应拦截器，处理认证失败的情况
    axios.interceptors.response.use(
        (response) => response,
        (error) => {
            // 如果是401未授权错误，自动登出
            if (error.response && error.response.status === 401) {
                authService.logout();
            }
            return Promise.reject(error);
        }
    );
}

// 自动设置拦截器
setupAuthInterceptor();

// 认证工具函数
const authUtils = {
    // 检查是否需要认证
    requireAuth() {
        if (!authService.isAuthenticated()) {
            window.location.href = '/login.html';
            return false;
        }
        return true;
    },
    
    // 检查是否需要管理员权限
    requireAdmin() {
        if (!authService.isAdmin()) {
            alert('需要管理员权限');
            window.history.back();
            return false;
        }
        return true;
    },
    
    // 检查权限并显示/隐藏元素
    applyPermissions() {
        // 为页面上带有data-permission属性的元素应用权限控制
        document.querySelectorAll('[data-permission]').forEach(element => {
            const permission = element.getAttribute('data-permission');
            if (!authService.hasPermission(permission)) {
                element.style.display = 'none';
            }
        });
        
        // 为需要管理员权限的元素应用控制
        document.querySelectorAll('[data-admin-only]').forEach(element => {
            if (!authService.isAdmin()) {
                element.style.display = 'none';
            }
        });
    }
};

// 挂载到window对象，使其全局可访问
window.authUtils = authUtils;