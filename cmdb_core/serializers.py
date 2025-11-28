from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Department, Server, NetworkDevice, Application, Service, Relationship, ClusterTemplate


class DepartmentSerializer(serializers.ModelSerializer):
    """部门序列化器"""
    
    class Meta:
        model = Department
        fields = [
            'id', 'name', 'parent', 'manager', 'contact', 'description',
            'created_at', 'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at')


class ServerSerializer(serializers.ModelSerializer):
    """服务器序列化器"""
    department_name = serializers.ReadOnlyField(source='department.name')
    
    class Meta:
        model = Server
        fields = [
            'id', 'name', 'hostname', 'ip_address', 'os_type', 'os_version',
            'cpu', 'memory', 'disk', 'status', 'department', 'department_name',
            'administrator', 'location', 'description', 'created_at', 'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at', 'department_name')


class NetworkDeviceSerializer(serializers.ModelSerializer):
    """网络设备序列化器"""
    department_name = serializers.ReadOnlyField(source='department.name')
    
    class Meta:
        model = NetworkDevice
        fields = [
            'id', 'name', 'device_type', 'ip_address', 'vendor', 'model',
            'serial_number', 'department', 'department_name', 'location',
            'administrator', 'description', 'created_at', 'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at', 'department_name')


class ApplicationSerializer(serializers.ModelSerializer):
    """应用序列化器"""
    department_name = serializers.ReadOnlyField(source='department.name')
    
    class Meta:
        model = Application
        fields = [
            'id', 'name', 'version', 'department', 'department_name',
            'owner', 'description', 'created_at', 'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at', 'department_name')


class ServiceSerializer(serializers.ModelSerializer):
    """服务序列化器"""
    application_name = serializers.ReadOnlyField(source='application.name')
    server_name = serializers.ReadOnlyField(source='server.name')
    server_ip = serializers.ReadOnlyField(source='server.ip_address')
    
    class Meta:
        model = Service
        fields = [
            'id', 'name', 'application', 'application_name', 'server',
            'server_name', 'server_ip', 'port', 'status', 'description',
            'created_at', 'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at', 'application_name', 'server_name', 'server_ip')


class RelationshipSerializer(serializers.ModelSerializer):
    """资源关系序列化器"""
    # 自定义字段用于显示和创建关系
    source_type = serializers.CharField(write_only=True)
    source_id = serializers.IntegerField(write_only=True)
    target_type = serializers.CharField(write_only=True)
    target_id = serializers.IntegerField(write_only=True)
    
    # 只读字段用于显示关系详情
    source_display = serializers.SerializerMethodField()
    target_display = serializers.SerializerMethodField()
    
    class Meta:
        model = Relationship
        fields = [
            'id', 'source_type', 'source_id', 'target_type', 'target_id',
            'source_display', 'target_display', 'relationship_type',
            'description', 'created_at', 'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at', 'source_display', 'target_display')
    
    def get_source_display(self, obj):
        """获取源资源的显示名称"""
        return str(obj.source)
    
    def get_target_display(self, obj):
        """获取目标资源的显示名称"""
        return str(obj.target)
    
    def create(self, validated_data):
        """创建关系时处理ContentType转换"""
        # 提取临时字段
        source_type = validated_data.pop('source_type')
        source_id = validated_data.pop('source_id')
        target_type = validated_data.pop('target_type')
        target_id = validated_data.pop('target_id')
        
        # 获取ContentType实例
        source_ct = ContentType.objects.get(model=source_type)
        target_ct = ContentType.objects.get(model=target_type)
        
        # 创建关系实例
        return Relationship.objects.create(
            source_content_type=source_ct,
            source_object_id=source_id,
            target_content_type=target_ct,
            target_object_id=target_id,
            **validated_data
        )
    
    def update(self, instance, validated_data):
        """更新关系时处理ContentType转换"""
        # 如果提供了新的源或目标，更新它们
        if 'source_type' in validated_data and 'source_id' in validated_data:
            source_type = validated_data.pop('source_type')
            source_id = validated_data.pop('source_id')
            source_ct = ContentType.objects.get(model=source_type)
            instance.source_content_type = source_ct
            instance.source_object_id = source_id
        
        if 'target_type' in validated_data and 'target_id' in validated_data:
            target_type = validated_data.pop('target_type')
            target_id = validated_data.pop('target_id')
            target_ct = ContentType.objects.get(model=target_type)
            instance.target_content_type = target_ct
            instance.target_object_id = target_id
        
        # 更新其他字段
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ClusterTemplateSerializer(serializers.ModelSerializer):
    """集群模板序列化器"""
    
    class Meta:
        model = ClusterTemplate
        fields = [
            'id', 'name', 'description', 'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at', 'created_by')