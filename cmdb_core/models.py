from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class Department(models.Model):
    """部门模型"""
    name = models.CharField(max_length=100, verbose_name='部门名称')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='上级部门')
    manager = models.CharField(max_length=100, blank=True, verbose_name='负责人')
    contact = models.CharField(max_length=100, blank=True, verbose_name='联系方式')
    description = models.TextField(blank=True, verbose_name='部门描述')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 添加通用关系
    relationships_as_source = GenericRelation('Relationship', related_query_name='source')
    relationships_as_target = GenericRelation('Relationship', related_query_name='target')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门管理'


class Server(models.Model):
    """服务器模型"""
    STATUS_CHOICES = (
        ('running', '运行中'),
        ('stopped', '已停止'),
        ('maintenance', '维护中'),
        ('fault', '故障'),
    )
    name = models.CharField(max_length=100, verbose_name='服务器名称')
    hostname = models.CharField(max_length=255, unique=True, verbose_name='主机名')
    ip_address = models.GenericIPAddressField(unique=True, verbose_name='IP地址')
    os_type = models.CharField(max_length=50, verbose_name='操作系统类型')
    os_version = models.CharField(max_length=50, verbose_name='操作系统版本')
    cpu = models.CharField(max_length=50, verbose_name='CPU信息')
    memory = models.CharField(max_length=50, verbose_name='内存信息')
    disk = models.CharField(max_length=100, verbose_name='磁盘信息')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='running', verbose_name='服务器状态')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属部门')
    administrator = models.CharField(max_length=100, blank=True, verbose_name='管理员')
    location = models.CharField(max_length=100, blank=True, verbose_name='物理位置')
    description = models.TextField(blank=True, verbose_name='服务器描述')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 添加通用关系
    relationships_as_source = GenericRelation('Relationship', related_query_name='source')
    relationships_as_target = GenericRelation('Relationship', related_query_name='target')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器管理'


class NetworkDevice(models.Model):
    """网络设备模型"""
    DEVICE_TYPES = (
        ('switch', '交换机'),
        ('router', '路由器'),
        ('firewall', '防火墙'),
        ('loadbalancer', '负载均衡器'),
        ('other', '其他'),
    )
    name = models.CharField(max_length=100, verbose_name='设备名称')
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES, verbose_name='设备类型')
    ip_address = models.GenericIPAddressField(unique=True, verbose_name='管理IP')
    vendor = models.CharField(max_length=50, verbose_name='厂商')
    model = models.CharField(max_length=50, verbose_name='型号')
    serial_number = models.CharField(max_length=100, blank=True, verbose_name='序列号')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属部门')
    location = models.CharField(max_length=100, blank=True, verbose_name='物理位置')
    administrator = models.CharField(max_length=100, blank=True, verbose_name='管理员')
    description = models.TextField(blank=True, verbose_name='设备描述')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 添加通用关系
    relationships_as_source = GenericRelation('Relationship', related_query_name='source')
    relationships_as_target = GenericRelation('Relationship', related_query_name='target')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '网络设备'
        verbose_name_plural = '网络设备管理'


class Application(models.Model):
    """应用模型"""
    name = models.CharField(max_length=100, verbose_name='应用名称')
    version = models.CharField(max_length=50, verbose_name='版本')
    description = models.TextField(blank=True, verbose_name='应用描述')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属部门')
    owner = models.CharField(max_length=100, blank=True, verbose_name='应用负责人')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 添加通用关系
    relationships_as_source = GenericRelation('Relationship', related_query_name='source')
    relationships_as_target = GenericRelation('Relationship', related_query_name='target')

    def __str__(self):
        return f"{self.name} ({self.version})"

    class Meta:
        verbose_name = '应用'
        verbose_name_plural = '应用管理'


class Service(models.Model):
    """服务模型"""
    STATUS_CHOICES = (
        ('running', '运行中'),
        ('stopped', '已停止'),
        ('maintenance', '维护中'),
        ('deploying', '部署中'),
    )
    name = models.CharField(max_length=100, verbose_name='服务名称')
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属应用')
    server = models.ForeignKey(Server, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='部署服务器')
    port = models.IntegerField(null=True, blank=True, verbose_name='服务端口')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='running', verbose_name='服务状态')
    description = models.TextField(blank=True, verbose_name='服务描述')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 添加通用关系
    relationships_as_source = GenericRelation('Relationship', related_query_name='source')
    relationships_as_target = GenericRelation('Relationship', related_query_name='target')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '服务'
        verbose_name_plural = '服务管理'


class Relationship(models.Model):
    """资源关系模型"""
    RELATIONSHIP_TYPES = (
        ('depends_on', '依赖'),
        ('hosts', '部署于'),
        ('connects_to', '连接到'),
        ('belongs_to', '属于'),
        ('manages', '管理'),
    )
    # 使用ContentType框架替代字符串类型
    source_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='source_relationships')
    source_object_id = models.PositiveIntegerField()
    source = GenericForeignKey('source_content_type', 'source_object_id')
    
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='target_relationships')
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    
    relationship_type = models.CharField(max_length=20, choices=RELATIONSHIP_TYPES, verbose_name='关系类型')
    description = models.TextField(blank=True, verbose_name='关系描述')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return f"{self.source} {self.relationship_type} {self.target}"

    class Meta:
        verbose_name = '资源关系'
        verbose_name_plural = '资源关系管理'


class ClusterTemplate(models.Model):
    """集群模板模型"""
    name = models.CharField(max_length=100, verbose_name='模板名称')
    description = models.TextField(blank=True, verbose_name='模板描述')
    created_by = models.CharField(max_length=100, default='admin', verbose_name='创建人')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '集群模板'
        verbose_name_plural = '集群模板管理'
