<template>
  <div class="business-topology-container">
    <!-- 页面标题 -->
    <h2>业务拓扑</h2>
    
    <!-- 主要内容区域 -->
    <div class="main-content-area">
      <!-- 左侧业务拓扑树 -->
      <div class="business-tree">
        <div class="tree-header">
          <input type="text" placeholder="请输入关键词" class="tree-search">
          <button class="search-btn"><i class="fas fa-search"></i></button>
        </div>
        <div class="tree-content">
          <div class="tree-node expanded">
            <div>
              <i class="fas fa-chevron-down"></i>
              <i class="fas fa-building"></i>
              <span class="node-name">官网业务</span>
            </div>
            <button class="new-btn">新建</button>
          </div>
          <div class="tree-node">
            <div>
              <i class="fas fa-chevron-right"></i>
              <i class="fas fa-server"></i>
              <span class="node-name">空闲机池</span>
              <span class="node-count">16</span>
            </div>
          </div>
          <div class="tree-node">
            <div>
              <i class="fas fa-chevron-right"></i>
              <i class="fas fa-map-marker-alt"></i>
              <span class="node-name">上海区</span>
              <span class="node-count">4</span>
            </div>
          </div>
          <div class="tree-node">
            <div>
              <i class="fas fa-chevron-right"></i>
              <i class="fas fa-map-marker-alt"></i>
              <span class="node-name">北京区</span>
              <span class="node-count">3</span>
            </div>
          </div>
          <div class="tree-node">
            <div>
              <i class="fas fa-chevron-right"></i>
              <i class="fas fa-map-marker-alt"></i>
              <span class="node-name">广东区</span>
              <span class="node-count">0</span>
            </div>
          </div>
          <div class="tree-node">
            <div>
              <i class="fas fa-chevron-right"></i>
              <i class="fas fa-map-marker-alt"></i>
              <span class="node-name">测试区域</span>
              <span class="node-count">0</span>
            </div>
          </div>
          <div class="tree-node">
            <div>
              <i class="fas fa-chevron-right"></i>
              <i class="fas fa-map-marker-alt"></i>
              <span class="node-name">湖南区</span>
              <span class="node-count">0</span>
            </div>
          </div>
          <div class="tree-node">
            <div>
              <i class="fas fa-chevron-right"></i>
              <i class="fas fa-map-marker-alt"></i>
              <span class="node-name">香港区</span>
              <span class="node-count">0</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- 右侧内容 -->
      <div class="right-content">
        <!-- 标签页 -->
        <div class="tabs">
          <span class="tab" :class="{ active: activeTab === 'host' }" @click="handleTabClick('host')">主机列表</span>
          <span class="tab" :class="{ active: activeTab === 'service' }" @click="handleTabClick('service')">服务实例</span>
          <span class="tab" :class="{ active: activeTab === 'node' }" @click="handleTabClick('node')">节点信息</span>
        </div>
        
        <!-- 操作按钮 -->
        <div class="operation-buttons">
          <button class="btn btn-primary" @click="handleAdd">新增</button>
          <button class="btn btn-secondary" @click="handleEdit">编辑</button>
          <button class="btn btn-secondary" @click="handleTransfer">转移到</button>
          <button class="btn btn-secondary" @click="handleCopy">复制</button>
          <button class="btn btn-secondary" @click="handleMore">更多</button>
          <div class="right-buttons">
            <select class="quick-select">
              <option>请选择收藏条件</option>
            </select>
            <button class="btn-icon" @click="handleDownload"><i class="fas fa-download"></i></button>
            <button class="btn-icon" @click="handleSettings"><i class="fas fa-cog"></i></button>
          </div>
        </div>
        
        <!-- 标签页内容 -->
        <!-- 主机列表 -->
        <div v-if="activeTab === 'host'">
          <!-- 主机列表表格 -->
          <div class="table-container">
            <table class="host-table">
              <thead>
                <tr>
                  <th><input type="checkbox"></th>
                  <th>内网IP <i class="fas fa-sort"></i></th>
                  <th>云区域</th>
                  <th>模块名</th>
                  <th>集群名</th>
                  <th>外网IP</th>
                  <th>主要维护人</th>
                  <th>备份维护人</th>
                  <th>机房2</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.30</td>
                  <td>default</td>
                  <td>db.db</td>
                  <td>上海区</td>
                  <td>-</td>
                  <td>admin</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.101</td>
                  <td>default</td>
                  <td>db.db</td>
                  <td>上海区</td>
                  <td>-</td>
                  <td>admin</td>
                  <td>admin</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.108</td>
                  <td>default</td>
                  <td>db.db</td>
                  <td>上海区</td>
                  <td>-</td>
                  <td>admin</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.150</td>
                  <td>default</td>
                  <td>空闲机</td>
                  <td>空闲机池</td>
                  <td>-</td>
                  <td>bence</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.160</td>
                  <td>default</td>
                  <td>空闲机</td>
                  <td>空闲机池</td>
                  <td>-</td>
                  <td>bence</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.196</td>
                  <td>default</td>
                  <td>空闲机</td>
                  <td>空闲机池</td>
                  <td>-</td>
                  <td>bence</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.36</td>
                  <td>default</td>
                  <td>空闲机</td>
                  <td>空闲机池</td>
                  <td>-</td>
                  <td>bence</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.89</td>
                  <td>default</td>
                  <td>空闲机</td>
                  <td>空闲机池</td>
                  <td>-</td>
                  <td>bence</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.119</td>
                  <td>default</td>
                  <td>空闲机</td>
                  <td>空闲机池</td>
                  <td>-</td>
                  <td>bence</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td><input type="checkbox"></td>
                  <td>192.168.1.197</td>
                  <td>default</td>
                  <td>空闲机</td>
                  <td>空闲机池</td>
                  <td>-</td>
                  <td>bence</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <!-- 分页 -->
          <div class="pagination">
            <span>共计20条 每页</span>
            <select class="page-size">
              <option>20</option>
            </select>
            <span>条</span>
            <span>已选择0条</span>
            <div class="page-buttons">
              <button class="btn-page"><i class="fas fa-chevron-left"></i></button>
              <button class="btn-page active">1</button>
              <button class="btn-page"><i class="fas fa-chevron-right"></i></button>
            </div>
          </div>
        </div>
        
        <!-- 服务实例 -->
        <div v-if="activeTab === 'service'" class="table-container">
          <table class="host-table">
            <thead>
              <tr>
                <th><input type="checkbox"></th>
                <th>服务实例名称</th>
                <th>服务类型</th>
                <th>状态</th>
                <th>所属集群</th>
                <th>所属模块</th>
                <th>创建时间</th>
                <th>更新时间</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><input type="checkbox"></td>
                <td>web-server-01</td>
                <td>Web服务</td>
                <td>运行中</td>
                <td>上海区</td>
                <td>web</td>
                <td>2023-01-01</td>
                <td>2023-01-02</td>
              </tr>
              <tr>
                <td><input type="checkbox"></td>
                <td>db-server-01</td>
                <td>数据库服务</td>
                <td>运行中</td>
                <td>上海区</td>
                <td>db</td>
                <td>2023-01-01</td>
                <td>2023-01-02</td>
              </tr>
            </tbody>
          </table>
          
          <!-- 分页 -->
          <div class="pagination">
            <span>共计2条 每页</span>
            <select class="page-size">
              <option>20</option>
            </select>
            <span>条</span>
            <span>已选择0条</span>
            <div class="page-buttons">
              <button class="btn-page"><i class="fas fa-chevron-left"></i></button>
              <button class="btn-page active">1</button>
              <button class="btn-page"><i class="fas fa-chevron-right"></i></button>
            </div>
          </div>
        </div>
        
        <!-- 节点信息 -->
        <div v-if="activeTab === 'node'" class="table-container">
          <table class="host-table">
            <thead>
              <tr>
                <th><input type="checkbox"></th>
                <th>节点名称</th>
                <th>节点类型</th>
                <th>状态</th>
                <th>IP地址</th>
                <th>所属区域</th>
                <th>创建时间</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><input type="checkbox"></td>
                <td>node-01</td>
                <td>物理机</td>
                <td>在线</td>
                <td>192.168.1.100</td>
                <td>上海区</td>
                <td>2023-01-01</td>
              </tr>
              <tr>
                <td><input type="checkbox"></td>
                <td>node-02</td>
                <td>物理机</td>
                <td>在线</td>
                <td>192.168.1.101</td>
                <td>上海区</td>
                <td>2023-01-01</td>
              </tr>
              <tr>
                <td><input type="checkbox"></td>
                <td>node-03</td>
                <td>虚拟机</td>
                <td>在线</td>
                <td>192.168.1.102</td>
                <td>北京区</td>
                <td>2023-01-01</td>
              </tr>
            </tbody>
          </table>
          
          <!-- 分页 -->
          <div class="pagination">
            <span>共计3条 每页</span>
            <select class="page-size">
              <option>20</option>
            </select>
            <span>条</span>
            <span>已选择0条</span>
            <div class="page-buttons">
              <button class="btn-page"><i class="fas fa-chevron-left"></i></button>
              <button class="btn-page active">1</button>
              <button class="btn-page"><i class="fas fa-chevron-right"></i></button>
            </div>
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
      // 业务拓扑数据
      businessTopology: [],
      // 主机列表数据
      hostList: [],
      // 加载状态
      loading: false,
      // 当前激活的标签页
      activeTab: 'host'
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
    },
    // 处理标签页点击事件
    handleTabClick(tabType) {
      this.activeTab = tabType
    },
    // 处理新增按钮点击事件
    handleAdd() {
      console.log('点击了新增按钮')
      alert('新增功能已触发')
    },
    // 处理编辑按钮点击事件
    handleEdit() {
      console.log('点击了编辑按钮')
      alert('编辑功能已触发')
    },
    // 处理转移到按钮点击事件
    handleTransfer() {
      console.log('点击了转移到按钮')
      alert('转移到功能已触发')
    },
    // 处理复制按钮点击事件
    handleCopy() {
      console.log('点击了复制按钮')
      alert('复制功能已触发')
    },
    // 处理更多按钮点击事件
    handleMore() {
      console.log('点击了更多按钮')
      alert('更多功能已触发')
    },
    // 处理下载按钮点击事件
    handleDownload() {
      console.log('点击了下载按钮')
      alert('下载功能已触发')
    },
    // 处理设置按钮点击事件
    handleSettings() {
      console.log('点击了设置按钮')
      alert('设置功能已触发')
    }
  }
}
</script>

<style scoped>
.business-topology-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}



/* 主要内容区域 */
.main-content-area {
  display: flex;
  gap: 20px;
}

/* 左侧业务拓扑树 */
.business-tree {
  width: 300px;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.tree-header {
  display: flex;
  padding: 12px;
  border-bottom: 1px solid #e4e7ed;
  background-color: #f5f7fa;
  align-items: center;
  gap: 0;
}

.tree-search {
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
}



.new-btn {
  margin-left: 8px;
  height: 32px;
  padding: 0 12px;
  border: none;
  background-color: #409eff;
  color: #fff;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.tree-content {
  padding: 12px;
  max-height: calc(100vh - 200px);
  overflow-y: auto;
}

.tree-node {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s;
  margin-bottom: 4px;
  justify-content: space-between;
}

.tree-node > div {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tree-node:hover {
  background-color: #ecf5ff;
}

.tree-node.expanded {
  background-color: #ecf5ff;
  border-left: 3px solid #409eff;
}

.tree-node i {
  font-size: 14px;
  color: #909399;
}

.tree-node .node-name {
  flex: 1;
  font-size: 14px;
  color: #303133;
}

.tree-node .node-count {
  font-size: 12px;
  color: #909399;
  background-color: #f5f7fa;
  padding: 2px 6px;
  border-radius: 10px;
}

/* 右侧内容 */
.right-content {
  flex: 1;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
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

/* 操作按钮 */
.operation-buttons {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  border-bottom: 1px solid #e4e7ed;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s;
  margin-right: 8px;
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

.right-buttons {
  display: flex;
  align-items: center;
  gap: 8px;
}

.quick-select {
  width: 150px;
  height: 32px;
  padding: 0 12px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  font-size: 14px;
}

.btn-icon {
  width: 32px;
  height: 32px;
  border: 1px solid #dcdfe6;
  background-color: #fff;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 主机列表表格 */
.table-container {
  overflow-x: auto;
  padding: 16px;
}

.host-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.host-table th,
.host-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #e4e7ed;
}

.host-table th {
  background-color: #f5f7fa;
  color: #303133;
  font-weight: 500;
}

.host-table td {
  color: #606266;
}

.host-table input[type="checkbox"] {
  cursor: pointer;
}

/* 分页 */
.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  border-top: 1px solid #e4e7ed;
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

.btn-page:hover:not(.active) {
  border-color: #409eff;
  color: #409eff;
}
</style>