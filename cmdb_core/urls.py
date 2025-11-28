from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet,
    ServerViewSet,
    NetworkDeviceViewSet,
    ApplicationViewSet,
    ServiceViewSet,
    RelationshipViewSet,
    login,
    register,
    get_user_info,
    logout
)

# 创建路由器
router = DefaultRouter()

# 注册视图集到路由器
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'servers', ServerViewSet, basename='server')
router.register(r'network-devices', NetworkDeviceViewSet, basename='network-device')
router.register(r'applications', ApplicationViewSet, basename='application')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'relationships', RelationshipViewSet, basename='relationship')

# API路由
urlpatterns = [
    path('', include(router.urls)),
    # 认证相关路由
    path('auth/login/', login, name='login'),
    path('auth/register/', register, name='register'),
    path('auth/user/', get_user_info, name='get_user_info'),
    path('auth/logout/', logout, name='logout'),
]