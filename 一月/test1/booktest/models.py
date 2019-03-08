from django.db import models


# Create your models here.
class ImageModel(models.Model):
    title = models.CharField(verbose_name='图片标题', max_length=64)
    image_url = models.ImageField(upload_to='static/media/')
