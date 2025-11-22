import os
import django

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cmdb_project.settings')
django.setup()

from django.contrib.auth.models import User

# 创建超级用户
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    print('超级用户创建成功！用户名: admin, 密码: admin123')
else:
    print('超级用户已存在')