from django.db import models

# Create your models here.
# 1.生成迁移文件  python manage.py makemigrations
# 2.执行迁移文件  python manage.py migrate
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=50)
