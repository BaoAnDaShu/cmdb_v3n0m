from rest_framework import viewsets, filters
from .models import Department, Server, NetworkDevice, Application, Service, Relationship
from .serializers import (
    DepartmentSerializer,
    ServerSerializer,
    NetworkDeviceSerializer,
    ApplicationSerializer,
    ServiceSerializer,
    RelationshipSerializer
)


class DepartmentViewSet(viewsets.ModelViewSet):
    """部门视图集"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'manager', 'contact']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']


class ServerViewSet(viewsets.ModelViewSet):
    """服务器视图集"""
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'hostname', 'ip_address', 'os_type', 'administrator']
    ordering_fields = ['name', 'created_at', 'updated_at', 'ip_address']
    ordering = ['name']


class NetworkDeviceViewSet(viewsets.ModelViewSet):
    """网络设备视图集"""
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'ip_address', 'vendor', 'model', 'serial_number']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']


class ApplicationViewSet(viewsets.ModelViewSet):
    """应用视图集"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'version', 'owner']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']


class ServiceViewSet(viewsets.ModelViewSet):
    """服务视图集"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'application__name', 'server__name']
    ordering_fields = ['name', 'created_at', 'updated_at']
    ordering = ['name']


class RelationshipViewSet(viewsets.ModelViewSet):
    """资源关系视图集"""
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['source_type', 'target_type', 'relationship_type']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['created_at']
