<template>
  <div class="service-template-container">
    <!-- 页面标题 -->
    <h2>服务模板</h2>
    
    <!-- 提示信息框 -->
    <div class="tip-box">
      <i class="fas fa-info-circle"></i>
      <span>服务模板可以定义业务使用的服务，用于业务拓扑中批量部署和变更服务实例。</span>
      <button class="close-btn"><i class="fas fa-times"></i></button>
    </div>
    
    <!-- 操作栏 -->
    <div class="action-bar">
      <button class="btn btn-primary">新建</button>
      <div class="filter-section">
        <select class="filter-select">
          <option>所有一级分类</option>
        </select>
        <select class="filter-select">
          <option>所有二级分类</option>
        </select>
        <input type="text" placeholder="请输入模板名称" class="search-input">
        <button class="search-btn"><i class="fas fa-search"></i></button>
      </div>
    </div>
    
    <!-- 服务模板列表 -->
    <div class="template-list">
      <table class="template-table">
        <thead>
          <tr>
            <th>ID <i class="fas fa-sort"></i></th>
            <th>模板名称 <i class="fas fa-sort"></i></th>
            <th>服务分类 <i class="fas fa-sort"></i></th>
            <th>进程数量 <i class="fas fa-sort"></i></th>
            <th>已使用模块数 <i class="fas fa-sort"></i></th>
            <th>修改人 <i class="fas fa-sort"></i></th>
            <th>修改时间 <i class="fas fa-sort"></i></th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>120</td>
            <td>Redis</td>
            <td>数据库/Redis</td>
            <td>1</td>
            <td>0</td>
            <td>admin</td>
            <td>2022-09-29 18:15</td>
            <td>
              <button class="btn-action edit">编辑</button>
              <button class="btn-action clone">克隆</button>
              <button class="btn-action delete">删除</button>
            </td>
          </tr>
          <tr>
            <td>119</td>
            <td>MySQL</td>
            <td>数据库/MySQL</td>
            <td>1</td>
            <td>0</td>
            <td>admin</td>
            <td>2022-09-29 18:14</td>
            <td>
              <button class="btn-action edit">编辑</button>
              <button class="btn-action clone">克隆</button>
              <button class="btn-action delete">删除</button>
            </td>
          </tr>
          <tr>
            <td>118</td>
            <td>Nginx</td>
            <td>HTTP服务/Nginx</td>
            <td>1</td>
            <td>0</td>
            <td>admin</td>
            <td>2022-09-29 18:14</td>
            <td>
              <button class="btn-action edit">编辑</button>
              <button class="btn-action clone">克隆</button>
              <button class="btn-action delete">删除</button>
            </td>
          </tr>
          <tr>
            <td>117</td>
            <td>Apache</td>
            <td>HTTP服务/Apache</td>
            <td>1</td>
            <td>0</td>
            <td>admin</td>
            <td>2022-09-29 18:13</td>
            <td>
              <button class="btn-action edit">编辑</button>
              <button class="btn-action clone">克隆</button>
              <button class="btn-action delete">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <!-- 分页 -->
    <div class="pagination">
      <span>共4条 每页</span>
      <select class="page-size">
        <option>20</option>
      </select>
      <span>条</span>
      <div class="page-buttons">
        <button class="btn-page disabled"><i class="fas fa-chevron-left"></i></button>
        <button class="btn-page active">1</button>
        <button class="btn-page disabled"><i class="fas fa-chevron-right"></i></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ServiceTemplate',
  data() {
    return {
      // 服务模板数据
      templates: [],
      // 加载状态
      loading: false
    }
  },
  mounted() {
    // 初始化数据
    this.initData()
  },
  methods: {
    initData() {
      // 这里可以添加数据获取逻辑
      this.loading = false
    }
  }
}
</script>

<style scoped>
.service-template-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

/* 顶部业务选择栏 */
.business-select-bar {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  background-color: #fff;
  padding: 12px 16px;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.business-select {
  width: 150px;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.3s;
  margin-right: 20px;
}

.business-select:focus {
  border-color: #409eff;
}

.business-select-bar h2 {
  margin: 0;
  font-size: 18px;
  color: #303133;
}

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

.filter-select {
  width: 150px;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.3s;
}

.filter-select:focus {
  border-color: #409eff;
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

/* 服务模板列表 */
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

.btn-action.clone {
  background-color: #f0f9eb;
  color: #67c23a;
}

.btn-action.clone:hover {
  background-color: #e1f3d8;
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

.page-size {
  width: 60px;
  height: 32px;
  padding: 0 8px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  margin: 0 8px;
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