<template>
  <div class="application-list-container">
    <h2>应用列表</h2>
    <div class="application-list">
      <div v-if="loading" class="loading">
        加载中...
      </div>
      <div v-else-if="applications.length === 0" class="empty">
        没有应用数据
      </div>
      <div v-else class="application-grid">
        <div v-for="app in applications" :key="app.id" class="application-card">
          <div class="application-header">
            <h3>{{ app.name }}</h3>
            <span class="version-badge">
              v{{ app.version }}
            </span>
          </div>
          <div class="application-info">
            <p><strong>所属部门:</strong> {{ app.department_name }}</p>
            <p><strong>负责人:</strong> {{ app.owner }}</p>
            <p v-if="app.description" class="description"><strong>描述:</strong> {{ app.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ApplicationList',
  data() {
    return {
      applications: [],
      loading: true
    }
  },
  mounted() {
    this.fetchApplications()
  },
  methods: {
    fetchApplications() {
      this.loading = true
      this.$axios.get('/applications/')
        .then(response => {
          this.applications = response.data.results || response.data
          this.loading = false
        })
        .catch(error => {
          console.error('获取应用数据失败:', error)
          this.loading = false
        })
    }
  }
}
</script>

<style scoped>
.application-list-container {
  padding: 20px;
}

.loading, .empty {
  text-align: center;
  padding: 40px;
  color: #909399;
}

.application-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.application-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.application-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
}

.application-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.application-header h3 {
  margin: 0;
  color: #303133;
  font-size: 18px;
}

.version-badge {
  padding: 4px 8px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: 500;
  background-color: #f6ffed;
  color: #52c41a;
  border: 1px solid #b7eb8f;
}

.application-info p {
  margin: 8px 0;
  color: #606266;
  font-size: 14px;
}

.application-info .description {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.application-info strong {
  color: #303133;
}
</style>