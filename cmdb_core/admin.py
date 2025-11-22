from django.contrib import admin
from .models import Department, Server, NetworkDevice, Application, Service, Relationship


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'contact', 'created_at')
    search_fields = ('name', 'manager')
    list_filter = ('created_at',)
    ordering = ('name',)


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'hostname', 'ip_address', 'status', 'department', 'created_at')
    search_fields = ('name', 'hostname', 'ip_address')
    list_filter = ('status', 'department', 'os_type', 'created_at')
    ordering = ('name',)


@admin.register(NetworkDevice)
class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_type', 'ip_address', 'vendor', 'model', 'department', 'created_at')
    search_fields = ('name', 'ip_address', 'serial_number')
    list_filter = ('device_type', 'vendor', 'department', 'created_at')
    ordering = ('name',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'department', 'owner', 'created_at')
    search_fields = ('name', 'version', 'owner')
    list_filter = ('department', 'created_at')
    ordering = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'application', 'server', 'port', 'status', 'created_at')
    search_fields = ('name',)
    list_filter = ('status', 'application', 'server', 'created_at')
    ordering = ('name',)


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('source_type', 'source_id', 'relationship_type', 'target_type', 'target_id', 'created_at')
    search_fields = ('source_type', 'target_type', 'relationship_type')
    list_filter = ('relationship_type', 'source_type', 'target_type', 'created_at')
    ordering = ('created_at',)
