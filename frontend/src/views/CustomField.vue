<template>
  <div class="custom-field-container">
    <!-- 页面标题 -->
    <h2>自定义字段</h2>
    
    <!-- 提示信息 -->
    <div class="tip-message">
      <i class="fas fa-info-circle"></i>
      <span>自定义字段：创建的业务专有字段，仅在该业务内生效（*为必填字段）</span>
      <button class="close-btn"><i class="fas fa-times"></i></button>
    </div>
    
    <!-- 标签页和按钮区域 -->
    <div class="header-actions">
      <!-- 标签页 -->
      <div class="tabs">
        <span class="tab active">集群</span>
        <span class="tab">模块</span>
        <span class="tab">主机</span>
      </div>
      
      <!-- 操作按钮 -->
      <div class="action-buttons">
        <button class="btn btn-primary">新增字段</button>
        <button class="btn btn-secondary">新建分组</button>
        <button class="btn btn-secondary">字段预览</button>
      </div>
    </div>
    
    <!-- 字段分组区域 -->
    <div class="field-groups">
      <!-- 基础信息分组 -->
      <div class="field-group">
        <div class="group-header">
          <i class="fas fa-chevron-down"></i>
          <span class="group-name">基础信息(7)</span>
        </div>
        <div class="group-content">
          <div class="field-item">
            <div class="field-label">
              <span class="field-name">集群名</span>
              <span class="required">*</span>
            </div>
            <div class="field-info">
              <span class="field-key">bk_cluster_name</span>
            </div>
          </div>
          <div class="field-item">
            <div class="field-label">
              <span class="field-name">备注</span>
            </div>
            <div class="field-info">
              <span class="field-key">description</span>
            </div>
          </div>
          <!-- 其他字段省略 -->
        </div>
      </div>
      
      <!-- 新建业务分组按钮 -->
      <div class="add-group-btn">
        <i class="fas fa-plus"></i>
        <span>新建业务分组</span>
      </div>
      
      <!-- 右侧字段搜索 -->
      <div class="field-search">
        <div class="search-item">
          <div class="search-label">服务状态</div>
          <div class="search-value">bk_service_status</div>
        </div>
        <div class="search-input-group">
          <input type="text" placeholder="请输入关键字" class="search-input">
          <button class="search-btn"><i class="fas fa-search"></i></button>
        </div>
      </div>
    </div>
    
    <!-- 新建分组弹窗 -->
    <div class="modal-overlay" v-if="showModal">
      <div class="modal">
        <div class="modal-header">
          <h4>新建分组</h4>
          <button class="close-btn" @click="closeModal"><i class="fas fa-times"></i></button>
        </div>
        <div class="modal-body">
          <div class="form-item">
            <label class="form-label">分组名称*</label>
            <input type="text" placeholder="请输入分组名称" class="form-input">
          </div>
          <div class="form-item">
            <label class="form-label">是否默认折叠</label>
            <div class="switch-container">
              <input type="checkbox" id="default-collapse" class="switch">
              <label for="default-collapse" class="switch-label"></label>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary" @click="submitModal">提交</button>
          <button class="btn btn-secondary" @click="closeModal">取消</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CustomField',
  data() {
    return {
      showModal: true // 默认显示弹窗，用于演示
    }
  },
  methods: {
    closeModal() {
      this.showModal = false
    },
    submitModal() {
      // 提交逻辑
      this.showModal = false
    }
  }
}
</script>

<style scoped>
.custom-field-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

/* 页面标题 */
h2 {
  margin: 0 0 16px 0;
  font-size: 18px;
  color: #303133;
}

/* 提示信息 */
.tip-message {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background-color: #ecf5ff;
  border: 1px solid #d9ecff;
  border-radius: 4px;
  margin-bottom: 16px;
}

.tip-message i {
  color: #409eff;
  font-size: 16px;
}

.tip-message span {
  flex: 1;
  font-size: 14px;
  color: #606266;
}

.close-btn {
  background: none;
  border: none;
  color: #909399;
  cursor: pointer;
  font-size: 14px;
  padding: 0;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all 0.3s;
}

.close-btn:hover {
  background-color: #fff;
  color: #606266;
}

/* 标签页和按钮区域 */
.header-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

/* 标签页 */
.tabs {
  display: flex;
  gap: 0;
  background-color: #fff;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.tab {
  padding: 10px 20px;
  cursor: pointer;
  font-size: 14px;
  color: #606266;
  border-bottom: 2px solid transparent;
  transition: all 0.3s;
}

.tab.active {
  color: #409eff;
  border-bottom-color: #409eff;
  background-color: #fff;
}

/* 操作按钮 */
.action-buttons {
  display: flex;
  gap: 8px;
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

.btn-secondary {
  background-color: #f0f2f5;
  color: #606266;
}

.btn:hover {
  opacity: 0.9;
}

/* 字段分组区域 */
.field-groups {
  display: flex;
  gap: 20px;
}

/* 左侧字段分组 */
.left-groups {
  flex: 1;
}

/* 字段分组 */
.field-group {
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 16px;
  overflow: hidden;
}

/* 分组头部 */
.group-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background-color: #f5f7fa;
  cursor: pointer;
  border-bottom: 1px solid #e4e7ed;
}

.group-header i {
  color: #909399;
  font-size: 14px;
}

.group-name {
  font-size: 14px;
  font-weight: 500;
  color: #303133;
}

/* 分组内容 */
.group-content {
  padding: 16px;
}

/* 字段项 */
.field-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid #f0f2f5;
}

.field-item:last-child {
  border-bottom: none;
}

.field-label {
  display: flex;
  align-items: center;
  gap: 4px;
}

.field-name {
  font-size: 14px;
  color: #303133;
}

.required {
  color: #f56c6c;
  font-size: 14px;
}

.field-info {
  font-size: 14px;
  color: #909399;
}

.field-key {
  background-color: #f5f7fa;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}

/* 新建业务分组按钮 */
.add-group-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background-color: #f5f7fa;
  border: 1px dashed #dcdfe6;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  color: #409eff;
  transition: all 0.3s;
  margin-bottom: 16px;
  width: fit-content;
}

.add-group-btn:hover {
  background-color: #ecf5ff;
  border-color: #409eff;
}

/* 右侧字段搜索 */
.field-search {
  width: 300px;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 16px;
}

.search-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f2f5;
}

.search-label {
  font-size: 14px;
  color: #303133;
}

.search-value {
  font-size: 12px;
  color: #909399;
  background-color: #f5f7fa;
  padding: 4px 8px;
  border-radius: 4px;
}

.search-input-group {
  display: flex;
  gap: 0;
}

.search-input {
  flex: 1;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px 0 0 4px;
  font-size: 14px;
  outline: none;
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
  color: #909399;
}

/* 弹窗样式 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  width: 400px;
  overflow: hidden;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  border-bottom: 1px solid #e4e7ed;
  background-color: #f5f7fa;
}

.modal-header h4 {
  margin: 0;
  font-size: 16px;
  font-weight: 500;
  color: #303133;
}

.modal-body {
  padding: 16px;
}

.form-item {
  margin-bottom: 16px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-size: 14px;
  color: #303133;
  font-weight: 500;
}

.form-input {
  width: 100%;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
}

/* 开关样式 */
.switch-container {
  display: flex;
  align-items: center;
  gap: 8px;
}

.switch {
  position: relative;
  width: 40px;
  height: 20px;
  -webkit-appearance: none;
  appearance: none;
  background-color: #dcdfe6;
  outline: none;
  border-radius: 20px;
  transition: all 0.3s;
  cursor: pointer;
}

.switch:checked {
  background-color: #409eff;
}

.switch::before {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  left: 2px;
  top: 2px;
  background-color: #fff;
  border-radius: 50%;
  transition: all 0.3s;
}

.switch:checked::before {
  left: 22px;
}

.switch-label {
  cursor: pointer;
  font-size: 14px;
  color: #606266;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  padding: 16px;
  border-top: 1px solid #e4e7ed;
  background-color: #f5f7fa;
}
</style>