<template>
  <div class="model-management">
    <!-- 面包屑导航 -->
    <div class="breadcrumb">
      <span>首页</span> &gt; <span>资源平台</span> &gt; <span>资源模型</span> &gt; <span class="current">模型管理</span>
    </div>
    
    <!-- 页面标题 -->
    <div class="page-header">
      <h2>模型管理</h2>
      <p>自定义资源的模型和字段，每个模型必须有一个父模型。</p>
    </div>
    
    <!-- 模型类型标签 -->
    <div class="model-type-tabs">
      <span class="tab active">资产模型</span>
      <span class="tab">应用模型</span>
      <span class="tab">组织模型</span>
      <span class="tab">其他</span>
      <span class="tab-badge">1</span>
    </div>
    
    <!-- 搜索和操作栏 -->
    <div class="search-and-actions">
      <div class="search-section">
        <label>搜索模型：</label>
        <input type="text" placeholder="请输入模型名称" class="search-input">
        <label>使用状态：</label>
        <select class="status-select">
          <option>全部</option>
          <option>可用</option>
          <option>不可用</option>
        </select>
      </div>
      <div class="action-buttons">
        <button class="btn btn-secondary">+ 新建分组</button>
        <button class="btn btn-primary">+ 新建模型</button>
      </div>
    </div>
    
    <!-- 模型列表 -->
    <div class="model-list">
      <div class="model-group">
        <div class="group-header">
          <i class="fas fa-folder"></i>
          <span>公有云(5)</span>
          <span class="group-count">4</span>
        </div>
        <div class="model-items">
          <div class="model-item">
            <i class="fas fa-cloud"></i>
            <div class="model-info">
              <div class="model-name">云账户</div>
              <div class="model-code">yunzhanghu</div>
            </div>
            <div class="model-actions">
              <i class="fas fa-pen"></i>
            </div>
          </div>
          <div class="model-item">
            <i class="fas fa-map-marker-alt"></i>
            <div class="model-info">
              <div class="model-name">可用区</div>
              <div class="model-code">keyongqu</div>
            </div>
            <div class="model-actions">
              <i class="fas fa-pen"></i>
            </div>
          </div>
          <div class="model-item">
            <i class="fas fa-server"></i>
            <div class="model-info">
              <div class="model-name">云主机</div>
              <div class="model-code">yunzhuji</div>
            </div>
            <div class="model-actions">
              <i class="fas fa-pen"></i>
            </div>
          </div>
          <div class="model-item">
            <i class="fas fa-sync-alt"></i>
            <div class="model-info">
              <div class="model-name">同步类型</div>
              <div class="model-code">tongbuleixing</div>
            </div>
            <div class="model-actions">
              <i class="fas fa-pen"></i>
            </div>
          </div>
          <div class="model-item">
            <i class="fas fa-search"></i>
            <div class="model-info">
              <div class="model-name">同步扫描类型</div>
              <div class="model-code">scantype</div>
            </div>
            <div class="model-actions">
              <i class="fas fa-pen"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModelManagement'
}
</script>

<style scoped>
.model-management {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

.breadcrumb {
  font-size: 14px;
  color: #606266;
  margin-bottom: 20px;
}

.breadcrumb .current {
  color: #303133;
  font-weight: 500;
}

.page-header {
  margin-bottom: 20px;
}

.page-header h2 {
  font-size: 20px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 8px;
}

.page-header p {
  font-size: 14px;
  color: #606266;
}

.model-type-tabs {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  background-color: #fff;
  padding: 0 20px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  height: 48px;
}

.model-type-tabs .tab {
  padding: 0 20px;
  height: 100%;
  display: flex;
  align-items: center;
  cursor: pointer;
  font-size: 14px;
  color: #606266;
  position: relative;
}

.model-type-tabs .tab.active {
  color: #409eff;
  font-weight: 500;
}

.model-type-tabs .tab-badge {
  background-color: #f56c6c;
  color: #fff;
  font-size: 12px;
  padding: 2px 6px;
  border-radius: 10px;
  margin-left: 5px;
}

.search-and-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  background-color: #fff;
  padding: 16px 20px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.search-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-section label {
  font-size: 14px;
  color: #606266;
}

.search-input {
  width: 200px;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.3s;
}

.search-input:focus {
  border-color: #409eff;
}

.status-select {
  width: 120px;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.3s;
}

.status-select:focus {
  border-color: #409eff;
}

.action-buttons {
  display: flex;
  gap: 12px;
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

.btn-secondary {
  background-color: #f0f2f5;
  color: #606266;
}

.btn-secondary:hover {
  background-color: #e4e7ed;
}

.model-list {
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.model-group {
  margin-bottom: 20px;
}

.group-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 500;
  color: #303133;
  margin-bottom: 16px;
}

.group-header i {
  font-size: 16px;
}

.group-count {
  background-color: #ecf5ff;
  color: #409eff;
  font-size: 12px;
  padding: 2px 6px;
  border-radius: 10px;
}

.model-items {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}

.model-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  border: 1px solid #e4e7ed;
  border-radius: 4px;
  transition: all 0.3s;
  cursor: pointer;
}

.model-item:hover {
  border-color: #409eff;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.model-item i {
  font-size: 24px;
  color: #409eff;
}

.model-info {
  flex: 1;
}

.model-name {
  font-size: 14px;
  font-weight: 500;
  color: #303133;
  margin-bottom: 4px;
}

.model-code {
  font-size: 12px;
  color: #909399;
}

.model-actions {
  opacity: 0;
  transition: opacity 0.3s;
}

.model-item:hover .model-actions {
  opacity: 1;
}

.model-actions i {
  font-size: 16px;
  color: #909399;
  cursor: pointer;
}

.model-actions i:hover {
  color: #409eff;
}
</style>