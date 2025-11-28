<template>
  <div class="host-auto-apply-container">
    <!-- 页面标题 -->
    <h2>主机属性自动应用</h2>
    
    <!-- 主要内容区域 -->
    <div class="main-content-area">
      <!-- 左侧业务拓扑树 -->
      <div class="business-tree">
        <!-- 顶部搜索和操作 -->
        <div class="tree-header">
          <input type="text" placeholder="关键字搜索" class="tree-search">
          <select class="batch-operation">
            <option>批量操作</option>
            <option>启用策略</option>
            <option>禁用策略</option>
          </select>
        </div>
        
        <!-- 标签页 -->
        <div class="tabs">
          <span class="tab active" @click="handleTabClick('business')">按业务拓扑</span>
          <span class="tab" @click="handleTabClick('service')">按服务模板</span>
          <span class="tab" @click="handleTabClick('recycle')">待回收</span>
        </div>
        
        <!-- 树内容 -->
        <div class="tree-content">
          <!-- 空闲机池 -->
          <div class="tree-node">
            <i class="fas fa-chevron-right"></i>
            <i class="fas fa-server"></i>
            <span class="node-name">空闲机池</span>
          </div>
          
          <!-- 待回收 -->
          <div class="tree-node expanded">
            <i class="fas fa-chevron-down"></i>
            <i class="fas fa-recycle"></i>
            <span class="node-name">待回收</span>
            <!-- 子节点 -->
            <div class="tree-children">
              <div class="tree-node">
                <i class="fas fa-chevron-right"></i>
                <i class="fas fa-exclamation-triangle"></i>
                <span class="node-name">故障机</span>
              </div>
              <div class="tree-node">
                <i class="fas fa-chevron-right"></i>
                <i class="fas fa-exclamation-triangle"></i>
                <span class="node-name">故障机</span>
              </div>
              <div class="tree-node">
                <i class="fas fa-chevron-right"></i>
                <i class="fas fa-exclamation-triangle"></i>
                <span class="node-name">空闲机</span>
              </div>
            </div>
          </div>
          
          <!-- 广东游戏一区 -->
          <div class="tree-node">
            <i class="fas fa-chevron-right"></i>
            <i class="fas fa-map-marker-alt"></i>
            <span class="node-name">广东游戏一区</span>
          </div>
          
          <!-- 华南省网门户 -->
          <div class="tree-node">
            <i class="fas fa-chevron-right"></i>
            <i class="fas fa-map-marker-alt"></i>
            <span class="node-name">华南省网门户</span>
          </div>
          
          <!-- 西北业务省网 -->
          <div class="tree-node">
            <i class="fas fa-chevron-right"></i>
            <i class="fas fa-map-marker-alt"></i>
            <span class="node-name">西北业务省网</span>
          </div>
        </div>
      </div>
      
      <!-- 右侧内容 -->
      <div class="right-content">
        <!-- 右侧内容区域 -->
        <div class="content-section">
          <div class="empty-state">
            <i class="fas fa-info-circle"></i>
            <p>当前模块未启用自动应用策略</p>
            <button class="btn btn-primary" @click="handleEnable">立即启用</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HostAutoApply',
  data() {
    return {
      // 当前激活的标签页
      activeTab: 'business'
    }
  },
  methods: {
    // 处理标签页点击事件
    handleTabClick(tabType) {
      this.activeTab = tabType
    },
    // 处理立即启用按钮点击事件
    handleEnable() {
      console.log('点击了立即启用按钮')
      alert('自动应用策略已启用')
    }
  }
}
</script>

<style scoped>
.host-auto-apply-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

/* 主要内容区域 */
.main-content-area {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

/* 左侧业务拓扑树 */
.business-tree {
  width: 300px;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

/* 树头部 */
.tree-header {
  display: flex;
  padding: 12px;
  border-bottom: 1px solid #e4e7ed;
  background-color: #f5f7fa;
  gap: 8px;
}

/* 搜索框 */
.tree-search {
  flex: 1;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
}

/* 批量操作 */
.batch-operation {
  width: 100px;
  height: 32px;
  padding: 0 8px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
  background-color: #fff;
}

/* 标签页 */
.tabs {
  display: flex;
  border-bottom: 1px solid #e4e7ed;
  background-color: #f5f7fa;
}

.tab {
  padding: 12px 20px;
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

/* 树内容 */
.tree-content {
  padding: 12px;
  max-height: calc(100vh - 200px);
  overflow-y: auto;
}

/* 树节点 */
.tree-node {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s;
  margin-bottom: 4px;
}

.tree-node:hover {
  background-color: #ecf5ff;
}

.tree-node.expanded {
  background-color: #ecf5ff;
  border-left: 3px solid #409eff;
}

/* 树节点图标 */
.tree-node i {
  font-size: 14px;
  color: #909399;
}

/* 树节点名称 */
.node-name {
  flex: 1;
  font-size: 14px;
  color: #303133;
}

/* 树子节点 */
.tree-children {
  margin-left: 24px;
  margin-top: 4px;
}

/* 右侧内容 */
.right-content {
  flex: 1;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

/* 内容区域 */
.content-section {
  padding: 20px;
  min-height: 400px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 空状态 */
.empty-state {
  text-align: center;
  color: #909399;
}

.empty-state i {
  font-size: 48px;
  margin-bottom: 16px;
  color: #c0c4cc;
}

.empty-state p {
  margin-bottom: 24px;
  font-size: 14px;
}

/* 按钮样式 */
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
</style>