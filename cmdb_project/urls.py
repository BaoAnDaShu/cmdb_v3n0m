"""
URL configuration for cmdb_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

# API文档配置
API_TITLE = 'CMDB系统 API'
API_DESCRIPTION = 'CMDB系统的RESTful API接口文档'

default_permission_classes = [permissions.AllowAny]

urlpatterns = [
    # 管理后台
    path('admin/', admin.site.urls),
    
    # API文档
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    
    # API路由
    path('api/', include('cmdb_core.urls')),
]
