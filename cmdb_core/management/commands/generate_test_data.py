from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from cmdb_core.models import (
    Department, Server, NetworkDevice, Application, Service, Relationship
)
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from faker import Faker
import random

fake = Faker('zh_CN')


class Command(BaseCommand):
    help = '生成CMDB系统测试数据'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='生成数据的数量')
        parser.add_argument('--clear', action='store_true', help='清空现有数据')

    def handle(self, *args, **options):
        count = options['count']
        clear = options['clear']
        
        self.stdout.write(self.style.SUCCESS(f'开始生成{count}条测试数据...'))
        
        # 清空现有数据
        if clear:
            self.stdout.write(self.style.WARNING('正在清空现有数据...'))
            # 使用原生SQL语句清空表，避免Django级联删除问题
            with connection.cursor() as cursor:
                # 禁用外键约束
                cursor.execute('PRAGMA foreign_keys = OFF')
                
                # 清空表数据，按依赖顺序
                cursor.execute('DELETE FROM cmdb_core_service')
                cursor.execute('DELETE FROM cmdb_core_application')
                cursor.execute('DELETE FROM cmdb_core_networkdevice')
                cursor.execute('DELETE FROM cmdb_core_server')
                cursor.execute('DELETE FROM cmdb_core_department')
                # 保留admin用户
                cursor.execute("DELETE FROM auth_user WHERE username != 'admin'")
                
                # 启用外键约束
                cursor.execute('PRAGMA foreign_keys = ON')
            self.stdout.write(self.style.SUCCESS('✓ 现有数据已清空'))
        
        # 1. 创建超级用户（如果不存在）
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✓ 创建超级用户: admin/admin123'))
        
        # 2. 创建普通用户
        # 先获取现有普通用户数量
        existing_users = User.objects.filter(username__startswith='user').count()
        for i in range(count):
            username = f'user{existing_users + i + 1}'
            User.objects.create_user(
                username=username,
                email=f'{username}@example.com',
                password='password123'
            )
        self.stdout.write(self.style.SUCCESS(f'✓ 创建{count}个普通用户'))
        
        # 3. 创建部门
        departments = []
        # 先创建顶级部门
        for i in range(3):
            dept = Department.objects.create(
                name=f'顶级部门{i+1}',
                manager=fake.name(),
                contact=fake.phone_number(),
                description=fake.text(max_nb_chars=100)
            )
            departments.append(dept)
        
        # 创建子部门
        for i in range(count - 3):
            parent = random.choice(departments)
            dept = Department.objects.create(
                name=f'{parent.name}-子部门{i+1}',
                parent=parent,
                manager=fake.name(),
                contact=fake.phone_number(),
                description=fake.text(max_nb_chars=100)
            )
            departments.append(dept)
        self.stdout.write(self.style.SUCCESS(f'✓ 创建{len(departments)}个部门'))
        
        # 4. 创建服务器
        servers = []
        for i in range(count):
            # 生成随机IP地址
            ip_address = f'{random.randint(1, 254)}.{random.randint(0, 254)}.{random.randint(0, 254)}.{random.randint(1, 254)}'
            server = Server.objects.create(
                name=f'服务器{i+1}',
                hostname=f'server{i+1}.example.com',
                ip_address=ip_address,
                os_type=random.choice(['Linux', 'Windows', 'macOS']),
                os_version=random.choice(['Ubuntu 20.04', 'CentOS 7', 'Windows Server 2019', 'macOS 12']),
                cpu=fake.text(max_nb_chars=20),
                memory=random.choice(['8GB', '16GB', '32GB', '64GB']),
                disk=random.choice(['256GB SSD', '512GB SSD', '1TB HDD', '2TB HDD']),
                status=random.choice(['running', 'stopped', 'maintenance', 'fault']),
                department=random.choice(departments),
                administrator=fake.name(),
                location=fake.address(),
                description=fake.text(max_nb_chars=100)
            )
            servers.append(server)
        self.stdout.write(self.style.SUCCESS(f'✓ 创建{len(servers)}台服务器'))
        
        # 5. 创建网络设备
        network_devices = []
        for i in range(count):
            # 生成随机IP地址
            ip_address = f'{random.randint(1, 254)}.{random.randint(0, 254)}.{random.randint(0, 254)}.{random.randint(1, 254)}'
            device = NetworkDevice.objects.create(
                name=f'网络设备{i+1}',
                device_type=random.choice(['switch', 'router', 'firewall', 'loadbalancer', 'other']),
                ip_address=ip_address,
                vendor=random.choice(['华为', '华三', '思科', ' Juniper', '锐捷']),
                model=fake.text(max_nb_chars=20),
                serial_number=fake.uuid4(),
                department=random.choice(departments),
                location=fake.address(),
                administrator=fake.name(),
                description=fake.text(max_nb_chars=100)
            )
            network_devices.append(device)
        self.stdout.write(self.style.SUCCESS(f'✓ 创建{len(network_devices)}台网络设备'))
        
        # 6. 创建应用
        applications = []
        for i in range(count):
            app = Application.objects.create(
                name=f'应用{i+1}',
                version=f'{random.randint(1, 3)}.{random.randint(0, 9)}.{random.randint(0, 99)}',
                department=random.choice(departments),
                owner=fake.name(),
                description=fake.text(max_nb_chars=100)
            )
            applications.append(app)
        self.stdout.write(self.style.SUCCESS(f'✓ 创建{len(applications)}个应用'))
        
        # 7. 创建服务
        services = []
        for i in range(count):
            service = Service.objects.create(
                name=f'服务{i+1}',
                application=random.choice(applications),
                server=random.choice(servers),
                port=random.randint(1000, 9999),
                status=random.choice(['running', 'stopped', 'maintenance', 'deploying']),
                description=fake.text(max_nb_chars=100)
            )
            services.append(service)
        self.stdout.write(self.style.SUCCESS(f'✓ 创建{len(services)}个服务'))
        
        # 8. 创建关系 - 跳过，因为数据库表结构问题
        self.stdout.write(self.style.SUCCESS(f'✓ 跳过创建关系（数据库表结构问题）'))
        
        self.stdout.write(self.style.SUCCESS('\n🎉 测试数据生成完成！'))
        self.stdout.write(self.style.SUCCESS('\n超级用户：'))
        self.stdout.write(self.style.SUCCESS('  用户名: admin'))
        self.stdout.write(self.style.SUCCESS('  密码: admin123'))
        self.stdout.write(self.style.SUCCESS('\n普通用户：'))
        self.stdout.write(self.style.SUCCESS('  用户名: user1 到 user{count}'))
        self.stdout.write(self.style.SUCCESS('  密码: password123'))
