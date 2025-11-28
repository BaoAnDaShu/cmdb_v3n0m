<template>
  <div class="service-category-container">
    <!-- 页面标题 -->
    <h2>服务分类</h2>
    
    <!-- 服务分类卡片区域 -->
    <div class="category-cards">
      <!-- 数据库分类 -->
      <div class="category-card">
        <div class="card-header">
          <span class="category-name">数据库</span>
          <span class="category-type">内置</span>
        </div>
        <div class="card-content">
          <ul class="service-list">
            <li>Etcd</li>
            <li>MongoDB</li>
            <li>Mysql</li>
            <li>Oracle</li>
            <li>Redis</li>
            <li>SQLServer</li>
            <li>Zookeeper</li>
          </ul>
        </div>
      </div>
      
      <!-- 消息队列分类 -->
      <div class="category-card">
        <div class="card-header">
          <span class="category-name">消息队列</span>
          <span class="category-type">内置</span>
        </div>
        <div class="card-content">
          <ul class="service-list">
            <li>Kafka</li>
            <li>RabbitMQ</li>
          </ul>
        </div>
      </div>
      
      <!-- HTTP服务分类 -->
      <div class="category-card">
        <div class="card-header">
          <span class="category-name">HTTP服务</span>
          <span class="category-type">内置</span>
        </div>
        <div class="card-content">
          <ul class="service-list">
            <li>Apache</li>
            <li>Nginx</li>
            <li>Tomcat</li>
          </ul>
        </div>
      </div>
      
      <!-- 存储分类 -->
      <div class="category-card">
        <div class="card-header">
          <span class="category-name">存储</span>
          <span class="category-type">内置</span>
        </div>
        <div class="card-content">
          <ul class="service-list">
            <li>Ceph</li>
            <li>NFS</li>
          </ul>
        </div>
      </div>
      
      <!-- 添加分类卡片 -->
      <div class="category-card add-card">
        <div class="add-icon">+</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ServiceCategory'
}
</script>

<style scoped>
.service-category-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

/* 页面标题 */
h2 {
  margin: 0 0 20px 0;
  font-size: 18px;
  color: #303133;
}

/* 服务分类卡片区域 */
.category-cards {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

/* 分类卡片 */
.category-card {
  width: calc(25% - 15px);
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
  min-height: 200px;
}

/* 卡片头部 */
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background-color: #f5f7fa;
  border-bottom: 1px solid #e4e7ed;
}

.category-name {
  font-size: 16px;
  font-weight: 500;
  color: #303133;
}

.category-type {
  font-size: 12px;
  color: #909399;
  background-color: #ecf5ff;
  padding: 2px 8px;
  border-radius: 10px;
}

/* 卡片内容 */
.card-content {
  padding: 16px;
}

/* 服务列表 */
.service-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.service-list li {
  padding: 6px 0;
  font-size: 14px;
  color: #606266;
  position: relative;
  padding-left: 16px;
}

.service-list li::before {
  content: "-";
  position: absolute;
  left: 8px;
  color: #909399;
}

/* 添加分类卡片 */
.add-card {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f5f7fa;
  border: 1px dashed #dcdfe6;
  cursor: pointer;
  transition: all 0.3s;
}

.add-card:hover {
  background-color: #ecf5ff;
  border-color: #409eff;
}

.add-icon {
  font-size: 32px;
  color: #909399;
  transition: all 0.3s;
}

.add-card:hover .add-icon {
  color: #409eff;
}
</style>