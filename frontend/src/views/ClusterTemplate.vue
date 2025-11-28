<template>
  <div class="cluster-template-container">
    <!-- 顶部业务选择栏 -->
    <h2>集群模板</h2>
    
    <!-- 提示信息框 -->
    <div class="tip-box">
      <i class="fas fa-info-circle"></i>
      <span>集群模板可以定义业务通用的集群结构，用于业务拓扑中快速部署和维护集群。</span>
      <button class="close-btn" @click="closeTip"><i class="fas fa-times"></i></button>
    </div>
    
    <!-- 操作栏 -->
    <div class="action-bar">
      <button class="btn btn-primary" @click="handleCreate">新建</button>
      <div class="filter-section">
        <input type="text" placeholder="请输入模板名称" class="search-input" v-model="searchKeyword">
        <button class="search-btn" @click="handleSearch"><i class="fas fa-search"></i></button>
      </div>
    </div>
    
    <!-- 集群模板列表 -->
    <div class="template-list">
      <table class="template-table">
        <thead>
          <tr>
            <th>模板名称 <i class="fas fa-sort"></i></th>
            <th>应用数量 <i class="fas fa-sort"></i></th>
            <th>修改人 <i class="fas fa-sort"></i></th>
            <th>修改时间 <i class="fas fa-sort"></i></th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="template in templates" :key="template.id">
            <td>{{ template.name }}</td>
            <td>{{ template.application_count || 0 }}</td>
            <td>{{ template.created_by }}</td>
            <td>{{ formatDate(template.updated_at) }}</td>
            <td>
              <button class="btn-action edit" @click="handleEdit(template)">编辑</button>
              <button class="btn-action delete" @click="handleDelete(template)">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <!-- 分页 -->
    <div class="pagination">
      <span>共{{ total }}条</span>
      <div class="page-buttons">
        <button class="btn-page" :class="{ disabled: currentPage === 1 }" @click="handlePageChange(currentPage - 1)">
          <i class="fas fa-chevron-left"></i>
        </button>
        <button class="btn-page" :class="{ active: currentPage === 1 }" @click="handlePageChange(1)">1</button>
        <button class="btn-page" :class="{ disabled: currentPage === 1 }" @click="handlePageChange(currentPage + 1)">
          <i class="fas fa-chevron-right"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ClusterTemplate',
  data() {
    return {
      // 集群模板数据
      templates: [],
      // 加载状态
      loading: false,
      // 搜索关键词
      searchKeyword: '',
      // 分页数据
      currentPage: 1,
      pageSize: 20,
      total: 0
    }
  },
  mounted() {
    // 初始化数据
    this.fetchClusterTemplates()
  },
  methods: {
    // 关闭提示框
    closeTip() {
      // 这里可以添加关闭提示框的逻辑
    },
    
    // 格式化日期
    formatDate(dateString) {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleString('zh-CN')
    },
    
    // 获取集群模板数据
    async fetchClusterTemplates() {
      this.loading = true
      try {
        const response = await this.$axios.get('/api/cluster-templates/')
        this.templates = response.data.results || response.data
        this.total = response.data.count || this.templates.length
      } catch (error) {
        console.error('获取集群模板失败:', error)
        this.$message.error('获取集群模板失败')
      } finally {
        this.loading = false
      }
    },
    
    // 新建模板
    handleCreate() {
      // 这里可以添加新建模板的逻辑
      console.log('新建模板')
    },
    
    // 编辑模板
    handleEdit(template) {
      // 这里可以添加编辑模板的逻辑
      console.log('编辑模板:', template)
    },
    
    // 删除模板
    async handleDelete(template) {
      if (confirm(`确定要删除模板"${template.name}"吗？`)) {
        try {
          await this.$axios.delete(`/api/cluster-templates/${template.id}/`)
          this.$message.success('删除成功')
          this.fetchClusterTemplates()
        } catch (error) {
          console.error('删除模板失败:', error)
          this.$message.error('删除模板失败')
        }
      }
    },
    
    // 搜索模板
    handleSearch() {
      this.currentPage = 1
      this.fetchClusterTemplates()
    },
    
    // 分页大小变化
    handlePageSizeChange() {
      this.currentPage = 1
      this.fetchClusterTemplates()
    },
    
    // 页码变化
    handlePageChange(page) {
      if (page < 1) return
      this.currentPage = page
      this.fetchClusterTemplates()
    }
  }
}
</script>

<style scoped>
.cluster-template-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

/* 页面标题 */


/* 提示信息框 */
.tip-box {
  display: flex;
  align-items: center;
  gap: 12px;
  background-color: #ecf5ff;
  border: 1px solid #d9ecff;
  border-radius: 4px;
  padding: 12px 16px;
  margin-bottom: 20px;
  font-size: 14px;
  color: #606266;
}

.tip-box i {
  color: #409eff;
  font-size: 16px;
}

.close-btn {
  margin-left: auto;
  background: none;
  border: none;
  cursor: pointer;
  color: #909399;
  font-size: 14px;
}

/* 操作栏 */
.action-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  padding: 16px;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-primary {
  background-color: #409eff;
  color: #fff;
}

.btn-primary:hover {
  background-color: #66b1ff;
}

.filter-section {
  display: flex;
  align-items: center;
  gap: 8px;
}



.search-input {
  width: 200px;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px 0 0 4px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.3s;
}

.search-input:focus {
  border-color: #409eff;
}

.search-btn {
  width: 32px;
  height: 32px;
  border: 1px solid #dcdfe6;
  border-left: none;
  background-color: #fff;
  cursor: pointer;
  border-radius: 0 4px 4px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #606266;
}

/* 集群模板列表 */
.template-list {
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 20px;
}

.template-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.template-table th,
.template-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #e4e7ed;
}

.template-table th {
  background-color: #f5f7fa;
  color: #303133;
  font-weight: 500;
  cursor: pointer;
}

.template-table th i {
  margin-left: 4px;
  font-size: 12px;
  color: #909399;
}

.template-table td {
  color: #606266;
}

/* 操作按钮 */
.btn-action {
  padding: 4px 8px;
  border: none;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
  margin-right: 4px;
  transition: all 0.3s;
}

.btn-action.edit {
  background-color: #ecf5ff;
  color: #409eff;
}

.btn-action.edit:hover {
  background-color: #d9ecff;
}

.btn-action.delete {
  background-color: #fef0f0;
  color: #f56c6c;
}

.btn-action.delete:hover {
  background-color: #fde2e2;
}

/* 分页 */
.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  padding: 16px;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  font-size: 14px;
  color: #606266;
}



.page-buttons {
  display: flex;
  gap: 8px;
}

.btn-page {
  width: 32px;
  height: 32px;
  border: 1px solid #dcdfe6;
  background-color: #fff;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  color: #606266;
}

.btn-page.active {
  background-color: #409eff;
  color: #fff;
  border-color: #409eff;
}

.btn-page:hover:not(.disabled) {
  border-color: #409eff;
  color: #409eff;
}

.btn-page.disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>