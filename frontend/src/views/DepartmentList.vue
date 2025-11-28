<template>
  <div class="department-list-container">
    <h2>部门列表</h2>
    <div class="department-list">
      <div v-if="loading" class="loading">
        加载中...
      </div>
      <div v-else-if="departments.length === 0" class="empty">
        没有部门数据
      </div>
      <div v-else class="department-grid">
        <div v-for="department in departments" :key="department.id" class="department-card">
          <div class="department-header">
            <h3>{{ department.name }}</h3>
            <span v-if="department.parent" class="parent-department">
              上级部门: {{ getParentName(department.parent) }}
            </span>
          </div>
          <div class="department-info">
            <p><strong>负责人:</strong> {{ department.manager }}</p>
            <p><strong>联系方式:</strong> {{ department.contact }}</p>
            <p v-if="department.description" class="description"><strong>描述:</strong> {{ department.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DepartmentList',
  data() {
    return {
      departments: [],
      loading: true
    }
  },
  mounted() {
    this.fetchDepartments()
  },
  methods: {
    fetchDepartments() {
      this.loading = true
      this.$axios.get('/departments/')
        .then(response => {
          this.departments = response.data.results || response.data
          this.loading = false
        })
        .catch(error => {
          console.error('获取部门数据失败:', error)
          this.loading = false
        })
    },
    getParentName(parentId) {
      const parent = this.departments.find(dept => dept.id === parentId)
      return parent ? parent.name : '未知部门'
    }
  }
}
</script>

<style scoped>
.department-list-container {
  padding: 20px;
}

.loading, .empty {
  text-align: center;
  padding: 40px;
  color: #909399;
}

.department-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.department-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.department-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
}

.department-header {
  margin-bottom: 15px;
}

.department-header h3 {
  margin: 0 0 8px 0;
  color: #303133;
  font-size: 18px;
}

.parent-department {
  font-size: 12px;
  color: #909399;
  background-color: #f5f7fa;
  padding: 2px 8px;
  border-radius: 10px;
}

.department-info p {
  margin: 8px 0;
  color: #606266;
  font-size: 14px;
}

.department-info .description {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.department-info strong {
  color: #303133;
}
</style>