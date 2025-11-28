<template>
  <div class="dynamic-group-container">
    <!-- 页面标题 -->
    <h2>动态分组</h2>
    
    <!-- 操作栏 -->
    <div class="action-bar">
      <button class="btn btn-primary">新建</button>
      <div class="search-section">
        <input type="text" placeholder="快速查询" class="search-input">
        <button class="search-btn"><i class="fas fa-search"></i></button>
      </div>
    </div>
    
    <!-- 动态分组列表 -->
    <div class="group-list">
      <table class="group-table">
        <thead>
          <tr>
            <th>分组名称 <i class="fas fa-sort"></i></th>
            <th>ID <i class="fas fa-sort"></i></th>
            <th>创建用户 <i class="fas fa-sort"></i></th>
            <th>创建时间 <i class="fas fa-sort"></i></th>
            <th>修改人 <i class="fas fa-sort"></i></th>
            <th>修改时间 <i class="fas fa-sort"></i></th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><a href="#" class="group-name">动态分组1</a></td>
            <td>bog13g1nbp37cq...</td>
            <td>admin</td>
            <td>2020-01-16 15:33:20</td>
            <td>admin</td>
            <td>2020-01-16 15:33:20</td>
            <td>
              <button class="btn-action preview">预览</button>
              <button class="btn-action edit">编辑</button>
              <button class="btn-action delete">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <!-- 分页 -->
    <div class="pagination">
      <span>共计1条 每页</span>
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
  name: 'DynamicGroup',
  data() {
    return {
      // 动态分组数据
      groups: [],
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
.dynamic-group-container {
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

.search-section {
  display: flex;
  align-items: center;
  gap: 0;
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

/* 动态分组列表 */
.group-list {
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 20px;
}

.group-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.group-table th,
.group-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #e4e7ed;
}

.group-table th {
  background-color: #f5f7fa;
  color: #303133;
  font-weight: 500;
  cursor: pointer;
}

.group-table th i {
  margin-left: 4px;
  font-size: 12px;
  color: #909399;
}

.group-table td {
  color: #606266;
}

.group-name {
  color: #409eff;
  text-decoration: none;
}

.group-name:hover {
  text-decoration: underline;
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

.btn-action.preview {
  background-color: #ecf5ff;
  color: #409eff;
}

.btn-action.preview:hover {
  background-color: #d9ecff;
}

.btn-action.edit {
  background-color: #f0f9eb;
  color: #67c23a;
}

.btn-action.edit:hover {
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