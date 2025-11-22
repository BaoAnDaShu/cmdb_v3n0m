# CMDB资产管理系统

## 项目介绍

CMDB (Configuration Management Database) 资产管理系统是一个企业级的IT资源管理平台，用于统一管理服务器、网络设备、应用、服务等IT资产，提供完整的资源生命周期管理、拓扑关系可视化、配置变更追踪等功能。

## 功能特性

### 资产管理
- 服务器资产管理（增删改查、状态监控、配置管理）
- 网络设备管理（交换机、路由器、防火墙等）
- 资产分类、标签管理
- 资产搜索与高级筛选

### 服务管理
- 应用管理（应用列表、配置、部署信息）
- 服务管理（服务依赖关系、运行状态）
- 服务拓扑图可视化

### 组织管理
- 部门层级结构管理
- 用户管理与权限控制
- 角色与权限分配

### 系统监控
- 仪表盘数据统计与图表展示
- 资源使用率监控
- 操作日志与审计跟踪

### 报表功能
- 资产统计报表
- 变更记录报表
- 自定义报表导出

## 技术栈

### 前端
- **框架**: Vue 3
- **UI组件库**: Element Plus
- **路由**: Vue Router
- **状态管理**: Vuex
- **HTTP请求**: Axios
- **图表库**: ECharts

### 后端
- **框架**: Django 4.x
- **ORM**: Django ORM
- **API**: Django REST Framework
- **数据库**: SQLite (开发环境), PostgreSQL/MySQL (生产环境)
- **认证**: Django Authentication
- **权限**: Django REST Framework Permissions

## 系统架构

- **前端**: SPA (Single Page Application)
- **后端**: RESTful API服务
- **数据库**: 关系型数据库
- **部署**: Docker容器化部署（推荐）

## 安装部署

### 开发环境设置

#### 后端设置

1. 克隆项目代码
```bash
git clone <repository_url>
cd cmdb
```

2. 创建并激活虚拟环境
```bash
python -m venv venv
# Windows
env\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 数据库迁移
```bash
python manage.py migrate
```

5. 创建超级用户
```bash
python create_superuser.py
```

6. 启动开发服务器
```bash
python manage.py runserver
```

#### 前端设置

1. 进入前端目录
```bash
cd frontend
```

2. 启动前端服务器（开发模式）
```bash
# 在项目根目录运行
python frontend_server.py
```

3. 访问系统
```
http://localhost:8080
```

### 生产环境部署

1. **后端部署**
   - 使用Gunicorn或uWSGI作为WSGI服务器
   - 配置Nginx作为反向代理
   - 设置环境变量和配置文件

2. **前端部署**
   - 构建前端项目
   - 将静态文件部署到CDN或Web服务器
   - 配置Nginx静态文件服务

3. **数据库配置**
   - 生产环境推荐使用PostgreSQL或MySQL
   - 配置数据库连接参数
   - 执行数据库迁移

4. **安全配置**
   - 配置HTTPS
   - 设置合理的权限控制
   - 配置日志记录

## 项目结构

```
cmdb/
├── cmdb_core/           # 核心应用
│   ├── models.py        # 数据模型
│   ├── serializers.py   # 序列化器
│   ├── views.py         # 视图
│   ├── urls.py          # URL路由
│   └── admin.py         # 后台管理
├── cmdb_project/        # 项目配置
│   ├── settings.py      # 全局配置
│   └── urls.py          # 主URL配置
├── frontend/            # 前端项目
│   ├── src/             # 源代码
│   ├── public/          # 静态资源
│   └── package.json     # 项目依赖
├── manage.py            # Django管理脚本
├── requirements.txt     # Python依赖
└── README.md            # 项目说明
```

## API文档

### 基础API路径
所有API端点都以`/api/`开头。

### 主要API端点

- **部门管理**: `/api/departments/`
- **用户管理**: `/api/users/`
- **服务器管理**: `/api/servers/`
- **网络设备管理**: `/api/network-devices/`
- **应用管理**: `/api/applications/`
- **服务管理**: `/api/services/`

详细的API文档可以通过访问以下地址获取：
```
http://localhost:8000/api/docs/
```

## 开发指南

### 后端开发

1. **创建新模型**
   - 在`cmdb_core/models.py`中定义数据模型
   - 运行`python manage.py makemigrations`生成迁移文件
   - 运行`python manage.py migrate`应用迁移

2. **创建API视图**
   - 在`cmdb_core/serializers.py`中创建序列化器
   - 在`cmdb_core/views.py`中创建视图
   - 在`cmdb_core/urls.py`中注册URL路由

### 前端开发

1. **创建新页面**
   - 在`frontend/src/views/`中创建Vue组件
   - 在`frontend/src/router/index.js`中注册路由
   - 在侧边栏中添加菜单项

2. **API调用**
   - 使用Axios发起HTTP请求
   - 处理响应数据和错误
   - 更新组件状态

## 测试

### 后端测试

```bash
python manage.py test cmdb_core
```

### 前端测试

```bash
cd frontend
npm run test
```

## 常见问题

1. **数据库连接失败**
   - 检查数据库配置是否正确
   - 确保数据库服务正在运行
   - 验证用户名和密码

2. **前端无法访问后端API**
   - 检查CORS配置
   - 确保后端服务器正在运行
   - 验证API URL是否正确

3. **权限错误**
   - 检查用户权限设置
   - 验证令牌是否有效
   - 确保请求头包含正确的认证信息

## 许可证

本项目采用MIT许可证。详见LICENSE文件。

## 联系信息

- **项目维护者**: [您的姓名/团队]
- **邮箱**: [contact@example.com]
- **GitHub**: [https://github.com/yourusername/cmdb](https://github.com/yourusername/cmdb)

## 致谢

感谢所有为本项目做出贡献的开发者和测试人员！