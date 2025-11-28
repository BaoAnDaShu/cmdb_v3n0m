<template>
  <div class="user-list-container">
    <h2>用户列表</h2>
    <div class="user-list">
      <div v-if="loading" class="loading">
        加载中...
      </div>
      <div v-else-if="users.length === 0" class="empty">
        没有用户数据
      </div>
      <div v-else class="user-grid">
        <div v-for="user in users" :key="user.id" class="user-card">
          <div class="user-header">
            <h3>{{ user.username }}</h3>
            <span class="role-badge" :class="user.role">
              {{ getRoleLabel(user.role) }}
            </span>
          </div>
          <div class="user-info">
            <p><strong>邮箱:</strong> {{ user.email }}</p>
            <p><strong>姓名:</strong> {{ user.name }}</p>
            <p><strong>部门:</strong> {{ user.department }}</p>
            <p><strong>状态:</strong> {{ user.is_active ? '活跃' : '禁用' }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserList',
  data() {
    return {
      users: [],
      loading: true
    }
  },
  mounted() {
    this.fetchUsers()
  },
  methods: {
    fetchUsers() {
      this.loading = true
      // 注意：这里的API端点可能需要根据实际后端实现进行调整
      this.$axios.get('/users/')
        .then(response => {
          this.users = response.data.results || response.data
          this.loading = false
        })
        .catch(error => {
          console.error('获取用户数据失败:', error)
          this.loading = false
        })
    },
    getRoleLabel(role) {
      const roleMap = {
        'admin': '管理员',
        'user': '普通用户',
        'viewer': '只读用户'
      }
      return roleMap[role] || role
    }
  }
}
</script>

<style scoped>
.user-list-container {
  padding: 20px;
}

.loading, .empty {
  text-align: center;
  padding: 40px;
  color: #909399;
}

.user-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.user-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.user-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
}

.user-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.user-header h3 {
  margin: 0;
  color: #303133;
  font-size: 18px;
}

.role-badge {
  padding: 4px 8px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: 500;
}

.role-badge.admin {
  background-color: #f0f5ff;
  color: #1890ff;
  border: 1px solid #adc6ff;
}

.role-badge.user {
  background-color: #f6ffed;
  color: #52c41a;
  border: 1px solid #b7eb8f;
}

.role-badge.viewer {
  background-color: #fff7e6;
  color: #fa8c16;
  border: 1px solid #ffe7ba;
}

.user-info p {
  margin: 8px 0;
  color: #606266;
  font-size: 14px;
}

.user-info strong {
  color: #303133;
}
</style>