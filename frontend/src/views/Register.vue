<template>
  <div class="register-container">
    <div class="register-form-wrapper">
      <div class="register-header">
        <h2>CMDB资产管理系统</h2>
        <p>创建新账户</p>
      </div>
      
      <el-form ref="registerForm" :model="registerForm" :rules="registerRules" class="register-form">
        <el-form-item prop="username">
          <el-input v-model="registerForm.username" placeholder="用户名" prefix-icon="User" />
        </el-form-item>
        
        <el-form-item prop="email">
          <el-input v-model="registerForm.email" placeholder="邮箱" prefix-icon="Message" />
        </el-form-item>
        
        <el-form-item prop="password">
          <el-input v-model="registerForm.password" type="password" placeholder="密码" prefix-icon="Lock" show-password />
        </el-form-item>
        
        <el-form-item prop="confirmPassword">
          <el-input v-model="registerForm.confirmPassword" type="password" placeholder="确认密码" prefix-icon="Lock" show-password />
        </el-form-item>
        
        <el-form-item>
          <el-button type="primary" :loading="loading" @click="handleRegister" class="register-btn">
            注册
          </el-button>
        </el-form-item>
        
        <div class="register-footer">
          <span>已有账户？</span>
          <el-button type="text" @click="$router.push('/login')">立即登录</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      registerForm: {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      },
      registerRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 20, message: '用户名长度在 3 到 20 个字符', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱格式', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, message: '密码长度不能少于6位', trigger: 'blur' }
        ],
        confirmPassword: [
          { required: true, message: '请确认密码', trigger: 'blur' },
          { trigger: 'blur' }
        ]
      },
      loading: false
    }
  },
  methods: {
    handleRegister() {
      this.$refs.registerForm.validate((valid) => {
        if (valid) {
          this.loading = true
          // 调用后端注册API
          const registerData = {
            username: this.registerForm.username,
            email: this.registerForm.email,
            password: this.registerForm.password
          }
          
          this.$axios.post('/auth/register/', registerData)
            .then(response => {
              this.loading = false
              this.$message.success('注册成功，请登录')
              this.$router.push('/login')
            })
            .catch(error => {
              this.loading = false
              let errorMsg = '注册失败'
              if (error.response?.data) {
                // 处理后端返回的错误信息
                const errors = error.response.data
                if (errors.username) errorMsg = errors.username[0]
                else if (errors.email) errorMsg = errors.email[0]
                else if (errors.password) errorMsg = errors.password[0]
                else errorMsg = JSON.stringify(errors)
              }
              this.$message.error(errorMsg)
            })
        }
      })
    },
    validateConfirmPassword(rule, value, callback) {
      if (value === '') {
        callback(new Error('请确认密码'))
      } else if (value !== this.registerForm.password) {
        callback(new Error('两次输入密码不一致'))
      } else {
        callback()
      }
    }
  },
  created() {
    // 设置确认密码验证规则的validator
    this.registerRules.confirmPassword[1].validator = this.validateConfirmPassword
  }
}
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f7fa;
}

.register-form-wrapper {
  width: 400px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 30px;
}

.register-header {
  text-align: center;
  margin-bottom: 30px;
}

.register-header h2 {
  font-size: 24px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 10px;
}

.register-header p {
  color: #909399;
  font-size: 14px;
}

.register-form {
  margin-top: 20px;
}

.register-btn {
  width: 100%;
  height: 40px;
  font-size: 16px;
}

.register-footer {
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #606266;
}
</style>