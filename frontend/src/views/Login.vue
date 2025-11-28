<template>
  <div class="login-container">
    <div class="login-form-wrapper">
      <div class="login-header">
        <h2>CMDB资产管理系统</h2>
        <p>登录您的账户</p>
      </div>
      
      <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form">
        <el-form-item prop="username">
          <el-input v-model="loginForm.username" placeholder="用户名" prefix-icon="User" />
        </el-form-item>
        
        <el-form-item prop="password">
          <el-input v-model="loginForm.password" type="password" placeholder="密码" prefix-icon="Lock" show-password />
        </el-form-item>
        
        <el-form-item>
          <el-button type="primary" :loading="loading" @click="handleLogin" class="login-btn">
            登录
          </el-button>
        </el-form-item>
        
        <div class="login-footer">
          <span>还没有账户？</span>
          <el-button type="text" @click="$router.push('/register')">立即注册</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      loginRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, message: '密码长度不能少于6位', trigger: 'blur' }
        ]
      },
      loading: false
    }
  },
  methods: {
    handleLogin() {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          this.loading = true
          // 调用后端登录API
          this.$axios.post('/auth/login/', this.loginForm)
            .then(response => {
              // 保存登录状态
              localStorage.setItem('token', response.data.token)
              localStorage.setItem('user', JSON.stringify({
                username: response.data.user.username,
                email: response.data.user.email,
                role: 'admin', // 这里可以根据后端返回的角色信息设置
                permissions: ['view_assets', 'edit_assets', 'manage_users', 'manage_roles']
              }))
              this.loading = false
              this.$message.success('登录成功')
              this.$router.push('/')
            })
            .catch(error => {
              this.loading = false
              this.$message.error('登录失败: ' + (error.response?.data?.detail || error.message))
            })
        }
      })
    }
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f7fa;
}

.login-form-wrapper {
  width: 400px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 30px;
}

.login-header {
  text-align: center;
  margin-bottom: 30px;
}

.login-header h2 {
  font-size: 24px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 10px;
}

.login-header p {
  color: #909399;
  font-size: 14px;
}

.login-form {
  margin-top: 20px;
}

.login-btn {
  width: 100%;
  height: 40px;
  font-size: 16px;
}

.login-footer {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #606266;
}
</style>