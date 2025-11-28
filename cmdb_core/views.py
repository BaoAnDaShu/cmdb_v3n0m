from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Department, Server, NetworkDevice, Application, Service, Relationship, ClusterTemplate
from .serializers import (
    DepartmentSerializer,
    ServerSerializer,
    NetworkDeviceSerializer,
    ApplicationSerializer,
    ServiceSerializer,
    RelationshipSerializer,
    ClusterTemplateSerializer
)


class DepartmentViewSet(viewsets.ModelViewSet):
    """部门视图集"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'manager', 'contact']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServerViewSet(viewsets.ModelViewSet):
    """服务器视图集"""
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'hostname', 'ip_address', 'os_type', 'administrator']
    ordering_fields = ['name', 'created_at', 'updated_at', 'ip_address']
    ordering = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class NetworkDeviceViewSet(viewsets.ModelViewSet):
    """网络设备视图集"""
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'ip_address', 'vendor', 'model', 'serial_number']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApplicationViewSet(viewsets.ModelViewSet):
    """应用视图集"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'version', 'owner']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceViewSet(viewsets.ModelViewSet):
    """服务视图集"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'application__name', 'server__name']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class RelationshipViewSet(viewsets.ModelViewSet):
    """资源关系视图集"""
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['relationship_type']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['created_at']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClusterTemplateViewSet(viewsets.ModelViewSet):
    """集群模板视图集"""
    queryset = ClusterTemplate.objects.all()
    serializer_class = ClusterTemplateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'created_by']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


# 认证相关API

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """用户登录API"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': '请提供用户名和密码'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    
    if not user:
        return Response(
            {'error': '用户名或密码错误'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    # 获取或创建Token
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'token': token.key,
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """用户注册API"""
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')
    first_name = request.data.get('first_name', '')
    last_name = request.data.get('last_name', '')
    
    if not username or not password:
        return Response(
            {'error': '请提供用户名和密码'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(username=username).exists():
        return Response(
            {'error': '用户名已存在'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # 创建用户
    user = User.objects.create(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=make_password(password)
    )
    
    # 创建Token
    token = Token.objects.create(user=user)
    
    return Response({
        'token': token.key,
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_user_info(request):
    """获取当前用户信息API"""
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name
    })


@api_view(['POST'])
def logout(request):
    """用户登出API"""
    # 删除Token
    request.auth.delete()
    return Response({'message': '登出成功'}, status=status.HTTP_200_OK)
