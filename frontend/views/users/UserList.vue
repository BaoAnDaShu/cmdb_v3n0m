<template>
  <div class="user-list-container">
    <el-card shadow="always">
      <template #header>
        <div class="card-header">
          <span>用户列表</span>
          <el-button type="primary" @click="handleAddUser">
            <el-icon><Plus /></el-icon>
            添加用户
          </el-button>
        </div>
      </template>
      
      <!-- 搜索和筛选 -->
      <div class="search-filter">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input
              v-model="searchQuery"
              placeholder="搜索用户名、姓名或邮箱"
              clearable
              @input="handleSearch"
              prefix-icon="el-icon-search"
            />
          </el-col>
          <el-col :span="6">
            <el-select
              v-model="selectedDepartment"
              placeholder="选择所属部门"
              clearable
              @change="handleFilter"
            >
              <el-option
                v-for="dept in departments"
                :key="dept.id"
                :label="dept.name"
                :value="dept.id"
              />
            </el-select>
          </el-col>
          <el-col :span="6">
            <el-select
              v-model="selectedRole"
              placeholder="选择角色"
              clearable
              @change="handleFilter"
            >
              <el-option label="超级管理员" value="admin" />
              <el-option label="普通用户" value="user" />
              <el-option label="只读用户" value="readonly" />
            </el-select>
          </el-col>
          <el-col :span="4">
            <el-button type="info" @click="resetFilters">
              <el-icon><Refresh /></el-icon>
              重置筛选
            </el-button>
          </el-col>
        </el-row>
      </div>
      
      <!-- 数据表格 -->
      <el-table
        v-loading="loading"
        :data="usersData"
        style="width: 100%"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55" />
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="username" label="用户名" width="120" />
        <el-table-column prop="fullname" label="姓名" width="100" />
        <el-table-column label="所属部门" width="150">
          <template #default="scope">
            {{ getDepartmentName(scope.row.department) }}
          </template>
        </el-table-column>
        <el-table-column prop="role" label="角色" width="100">
          <template #default="scope">
            <el-tag
              :type="getRoleTagType(scope.row.role)"
              :effect="getRoleTagEffect(scope.row.role)"
            >
              {{ getRoleText(scope.row.role) }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="email" label="邮箱" width="180" />
        <el-table-column prop="phone" label="电话" width="120" />
        <el-table-column prop="status" label="状态" width="100">
          <template #default="scope">
            <el-switch
              v-model="scope.row.status"
              active-color="#13ce66"
              inactive-color="#ff4949"
              :active-value="'active'"
              :inactive-value="'inactive'"
              @change="(value) => handleStatusChange(scope.row, value)"
            />
          </template>
        </el-table-column>
        <el-table-column prop="last_login" label="最后登录" width="180">
          <template #default="scope">
            {{ formatDate(scope.row.last_login) }}
          </template>
        </el-table-column>
        <el-table-column prop="created_at" label="创建时间" width="180">
          <template #default="scope">
            {{ formatDate(scope.row.created_at) }}
          </template>
        </el-table-column>
        <el-table-column label="操作" width="180" fixed="right">
          <template #default="scope">
            <el-button type="primary" size="small" @click="handleEditUser(scope.row)">
              <el-icon><Edit /></el-icon>
              编辑
            </el-button>
            <el-button type="info" size="small" @click="handleResetPassword(scope.row)">
              <el-icon><Key /></el-icon>
              重置密码
            </el-button>
            <el-button type="danger" size="small" @click="handleDeleteUser(scope.row)">
              <el-icon><Delete /></el-icon>
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      
      <!-- 分页 -->
      <div class="pagination-container">
        <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :page-sizes="[10, 20, 50, 100]"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />
      </div>
    </el-card>
    
    <!-- 添加/编辑用户对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="600px"
      @close="handleDialogClose"
    >
      <el-form
        ref="userFormRef"
        :model="userForm"
        :rules="formRules"
        label-width="120px"
      >
        <el-form-item label="用户名" prop="username">
          <el-input v-model="userForm.username" :disabled="!!editingUser" placeholder="请输入用户名" />
        </el-form-item>
        <template v-if="!editingUser">
          <el-form-item label="密码" prop="password">
            <el-input v-model="userForm.password" type="password" placeholder="请输入密码" />
          </el-form-item>
          <el-form-item label="确认密码" prop="confirm_password">
            <el-input v-model="userForm.confirm_password" type="password" placeholder="请确认密码" />
          </el-form-item>
        </template>
        <el-form-item label="姓名" prop="fullname">
          <el-input v-model="userForm.fullname" placeholder="请输入姓名" />
        </el-form-item>
        <el-form-item label="所属部门" prop="department">
          <el-select v-model="userForm.department" placeholder="请选择所属部门">
            <el-option
              v-for="dept in departments"
              :key="dept.id"
              :label="dept.name"
              :value="dept.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="角色" prop="role">
          <el-select v-model="userForm.role" placeholder="请选择角色">
            <el-option label="超级管理员" value="admin" />
            <el-option label="普通用户" value="user" />
            <el-option label="只读用户" value="readonly" />
          </el-select>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="userForm.email" placeholder="请输入邮箱地址" />
        </el-form-item>
        <el-form-item label="电话">
          <el-input v-model="userForm.phone" placeholder="请输入电话号码" />
        </el-form-item>
        <el-form-item label="状态">
          <el-switch
            v-model="userForm.status"
            active-color="#13ce66"
            inactive-color="#ff4949"
            :active-value="'active'"
            :inactive-value="'inactive'"
          />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="handleSubmitForm">确定</el-button>
        </span>
      </template>
    </el-dialog>
    
    <!-- 重置密码对话框 -->
    <el-dialog
      v-model="resetPasswordVisible"
      title="重置密码"
      width="400px"
      @close="handleResetPasswordClose"
    >
      <el-form
        ref="resetPasswordFormRef"
        :model="resetPasswordForm"
        :rules="resetPasswordRules"
        label-width="120px"
      >
        <el-form-item label="新密码" prop="new_password">
          <el-input v-model="resetPasswordForm.new_password" type="password" placeholder="请输入新密码" />
        </el-form-item>
        <el-form-item label="确认密码" prop="confirm_password">
          <el-input v-model="resetPasswordForm.confirm_password" type="password" placeholder="请确认新密码" />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="resetPasswordVisible = false">取消</el-button>
          <el-button type="primary" @click="handleResetPasswordSubmit">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { ref, reactive, onMounted, computed, watch } from 'vue'
import {
  Plus,
  Edit,
  Delete,
  Refresh,
  Search,
  Key
} from '@element-plus/icons-vue'

export default {
  name: 'UserList',
  components: {
    Plus,
    Edit,
    Delete,
    Refresh,
    Search,
    Key
  },
  setup() {
    // 状态
    const loading = ref(false)
    const users = ref([])
    const departments = ref([])
    const searchQuery = ref('')
    const selectedDepartment = ref('')
    const selectedRole = ref('')
    const currentPage = ref(1)
    const pageSize = ref(10)
    const total = ref(0)
    const multipleSelection = ref([])
    
    // 对话框相关
    const dialogVisible = ref(false)
    const editingUser = ref(null)
    const resetPasswordVisible = ref(false)
    const userToResetPassword = ref(null)
    
    // 表单数据
    const userForm = reactive({
      username: '',
      password: '',
      confirm_password: '',
      fullname: '',
      department: '',
      role: 'user',
      email: '',
      phone: '',
      status: 'active'
    })
    
    // 重置密码表单
    const resetPasswordForm = reactive({
      new_password: '',
      confirm_password: ''
    })
    
    // 表单验证规则
    const formRules = {
      username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
      password: [{ 
        validator: (rule, value, callback) => {
          if (editingUser.value) {
            callback()
          } else if (!value) {
            callback(new Error('请输入密码'))
          } else {
            callback()
          }
        }, 
        trigger: 'blur' 
      }],
      confirm_password: [{ 
        validator: (rule, value, callback) => {
          if (editingUser.value) {
            callback()
          } else if (!value) {
            callback(new Error('请确认密码'))
          } else if (value !== userForm.password) {
            callback(new Error('两次输入的密码不一致'))
          } else {
            callback()
          }
        }, 
        trigger: 'blur' 
      }],
      fullname: [{ required: true, message: '请输入姓名', trigger: 'blur' }],
      department: [{ required: true, message: '请选择所属部门', trigger: 'change' }],
      role: [{ required: true, message: '请选择角色', trigger: 'change' }]
    }
    
    // 重置密码表单验证规则
    const resetPasswordRules = {
      new_password: [{ required: true, message: '请输入新密码', trigger: 'blur' }],
      confirm_password: [{ 
        validator: (rule, value, callback) => {
          if (!value) {
            callback(new Error('请确认密码'))
          } else if (value !== resetPasswordForm.new_password) {
            callback(new Error('两次输入的密码不一致'))
          } else {
            callback()
          }
        }, 
        trigger: 'blur' 
      }]
    }
    
    // 计算属性：过滤后的数据
    const usersData = computed(() => {
      let filtered = [...users.value]
      
      // 按搜索词筛选
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(user => 
          user.username?.toLowerCase().includes(query) ||
          user.fullname?.toLowerCase().includes(query) ||
          user.email?.toLowerCase().includes(query)
        )
      }
      
      // 按部门筛选
      if (selectedDepartment.value) {
        filtered = filtered.filter(user => 
          user.department === selectedDepartment.value
        )
      }
      
      // 按角色筛选
      if (selectedRole.value) {
        filtered = filtered.filter(user => 
          user.role === selectedRole.value
        )
      }
      
      // 更新总数
      total.value = filtered.length
      
      // 分页
      const startIndex = (currentPage.value - 1) * pageSize.value
      const endIndex = startIndex + pageSize.value
      return filtered.slice(startIndex, endIndex)
    })
    
    // 获取对话框标题
    const dialogTitle = computed(() => {
      return editingUser.value ? '编辑用户' : '添加用户'
    })
    
    // 加载用户数据
    const loadUsers = async () => {
      loading.value = true
      try {
        const response = await axios.get('/users/')
        users.value = response.data.results || []
      } catch (error) {
        console.error('加载用户数据失败:', error)
        ElMessage.error('加载用户数据失败')
      } finally {
        loading.value = false
      }
    }
    
    // 加载部门数据
    const loadDepartments = async () => {
      try {
        const response = await axios.get('/departments/')
        departments.value = response.data.results || []
      } catch (error) {
        console.error('加载部门数据失败:', error)
        ElMessage.error('加载部门数据失败')
      }
    }
    
    // 处理搜索
    const handleSearch = () => {
      currentPage.value = 1
    }
    
    // 处理筛选
    const handleFilter = () => {
      currentPage.value = 1
    }
    
    // 重置筛选条件
    const resetFilters = () => {
      searchQuery.value = ''
      selectedDepartment.value = ''
      selectedRole.value = ''
      currentPage.value = 1
    }
    
    // 处理添加用户
    const handleAddUser = () => {
      editingUser.value = null
      resetForm()
      dialogVisible.value = true
    }
    
    // 处理编辑用户
    const handleEditUser = (user) => {
      editingUser.value = user
      // 填充表单数据
      Object.assign(userForm, {
        username: user.username || '',
        fullname: user.fullname || '',
        department: user.department || '',
        role: user.role || 'user',
        email: user.email || '',
        phone: user.phone || '',
        status: user.status || 'active'
      })
      dialogVisible.value = true
    }
    
    // 重置表单
    const resetForm = () => {
      Object.assign(userForm, {
        username: '',
        password: '',
        confirm_password: '',
        fullname: '',
        department: '',
        role: 'user',
        email: '',
        phone: '',
        status: 'active'
      })
    }
    
    // 处理表单提交
    const handleSubmitForm = async () => {
      try {
        // 处理空值（将空字符串转换为null）
        const formData = { ...userForm }
        // 编辑时移除密码字段
        if (editingUser.value) {
          delete formData.password
          delete formData.confirm_password
        }
        
        if (editingUser.value) {
          // 更新用户
          await axios.put(`/users/${editingUser.value.id}/`, formData)
          ElMessage.success('用户更新成功')
        } else {
          // 添加用户
          await axios.post('/users/', formData)
          ElMessage.success('用户添加成功')
        }
        dialogVisible.value = false
        loadUsers() // 重新加载数据
      } catch (error) {
        console.error('提交表单失败:', error)
        ElMessage.error('操作失败，请重试')
      }
    }
    
    // 处理删除用户
    const handleDeleteUser = (user) => {
      if (user.username === 'admin') {
        ElMessage.warning('不能删除超级管理员账户')
        return
      }
      
      ElMessageBox.confirm(
        `确定要删除用户「${user.username}」吗？`,
        '删除确认',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      ).then(async () => {
        try {
          await axios.delete(`/users/${user.id}/`)
          ElMessage.success('删除成功')
          loadUsers() // 重新加载数据
        } catch (error) {
          console.error('删除用户失败:', error)
          ElMessage.error('删除失败，请重试')
        }
      }).catch(() => {
        // 取消删除
      })
    }
    
    // 处理重置密码
    const handleResetPassword = (user) => {
      if (user.username === 'admin') {
        ElMessage.warning('不能重置超级管理员密码')
        return
      }
      userToResetPassword.value = user
      resetPasswordForm.new_password = ''
      resetPasswordForm.confirm_password = ''
      resetPasswordVisible.value = true
    }
    
    // 处理重置密码提交
    const handleResetPasswordSubmit = async () => {
      try {
        if (!userToResetPassword.value) return
        
        await axios.patch(`/users/${userToResetPassword.value.id}/reset-password/`, {
          new_password: resetPasswordForm.new_password
        })
        
        ElMessage.success('密码重置成功')
        resetPasswordVisible.value = false
        userToResetPassword.value = null
      } catch (error) {
        console.error('重置密码失败:', error)
        ElMessage.error('重置密码失败，请重试')
      }
    }
    
    // 处理选择变化
    const handleSelectionChange = (val) => {
      multipleSelection.value = val
    }
    
    // 处理状态变化
    const handleStatusChange = async (user, newStatus) => {
      try {
        if (user.username === 'admin') {
          ElMessage.warning('不能修改超级管理员状态')
          // 恢复原状态
          setTimeout(() => {
            user.status = 'active'
          }, 0)
          return
        }
        
        await axios.patch(`/users/${user.id}/`, { status: newStatus })
        ElMessage.success('状态更新成功')
      } catch (error) {
        console.error('更新状态失败:', error)
        ElMessage.error('更新状态失败，请重试')
        // 恢复原状态
        setTimeout(() => {
          user.status = user.status === 'active' ? 'inactive' : 'active'
        }, 0)
      }
    }
    
    // 分页处理
    const handleSizeChange = (size) => {
      pageSize.value = size
      currentPage.value = 1
    }
    
    const handleCurrentChange = (current) => {
      currentPage.value = current
    }
    
    // 格式化日期
    const formatDate = (dateString) => {
      if (!dateString) return '-'
      const date = new Date(dateString)
      return date.toLocaleString('zh-CN')
    }
    
    // 获取部门名称
    const getDepartmentName = (departmentId) => {
      if (!departmentId) return '-'
      const dept = departments.value.find(d => d.id === departmentId)
      return dept ? dept.name : '-'
    }
    
    // 获取角色标签类型
    const getRoleTagType = (role) => {
      switch (role) {
        case 'admin': return 'danger'
        case 'user': return 'primary'
        case 'readonly': return 'info'
        default: return 'info'
      }
    }
    
    // 获取角色标签效果
    const getRoleTagEffect = (role) => {
      return role === 'admin' ? 'dark' : 'plain'
    }
    
    // 获取角色文本
    const getRoleText = (role) => {
      switch (role) {
        case 'admin': return '超级管理员'
        case 'user': return '普通用户'
        case 'readonly': return '只读用户'
        default: return role
      }
    }
    
    // 对话框关闭处理
    const handleDialogClose = () => {
      resetForm()
      editingUser.value = null
    }
    
    // 重置密码对话框关闭处理
    const handleResetPasswordClose = () => {
      userToResetPassword.value = null
      resetPasswordForm.new_password = ''
      resetPasswordForm.confirm_password = ''
    }
    
    // 组件挂载时加载数据
    onMounted(() => {
      loadDepartments()
      loadUsers()
    })
    
    return {
      loading,
      usersData,
      departments,
      searchQuery,
      selectedDepartment,
      selectedRole,
      currentPage,
      pageSize,
      total,
      multipleSelection,
      dialogVisible,
      dialogTitle,
      userForm,
      formRules,
      resetPasswordVisible,
      resetPasswordForm,
      resetPasswordRules,
      handleAddUser,
      handleEditUser,
      handleDeleteUser,
      handleSubmitForm,
      handleResetPassword,
      handleResetPasswordSubmit,
      handleSearch,
      handleFilter,
      resetFilters,
      handleSelectionChange,
      handleStatusChange,
      handleSizeChange,
      handleCurrentChange,
      formatDate,
      getDepartmentName,
      getRoleTagType,
      getRoleTagEffect,
      getRoleText,
      handleDialogClose,
      handleResetPasswordClose
    }
  }
}
</script>

<style scoped>
.user-list-container {
  padding: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.search-filter {
  margin-bottom: 20px;
  padding: 15px;
  background-color: #f5f7fa;
  border-radius: 4px;
}

.pagination-container {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
}
</style>