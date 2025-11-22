from rest_framework import serializers
from .models import Department, Server, NetworkDevice, Application, Service, Relationship


class DepartmentSerializer(serializers.ModelSerializer):
    """部门序列化器"""
    
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ServerSerializer(serializers.ModelSerializer):
    """服务器序列化器"""
    department_name = serializers.ReadOnlyField(source='department.name')
    
    class Meta:
        model = Server
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class NetworkDeviceSerializer(serializers.ModelSerializer):
    """网络设备序列化器"""
    department_name = serializers.ReadOnlyField(source='department.name')
    
    class Meta:
        model = NetworkDevice
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ApplicationSerializer(serializers.ModelSerializer):
    """应用序列化器"""
    department_name = serializers.ReadOnlyField(source='department.name')
    
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ServiceSerializer(serializers.ModelSerializer):
    """服务序列化器"""
    application_name = serializers.ReadOnlyField(source='application.name')
    server_name = serializers.ReadOnlyField(source='server.name')
    server_ip = serializers.ReadOnlyField(source='server.ip_address')
    
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class RelationshipSerializer(serializers.ModelSerializer):
    """资源关系序列化器"""
    
    class Meta:
        model = Relationship
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')