from django.db import models
from django.conf import settings
# Create your models here.
class About(models.Model):
    image = models.ImageField(upload_to='about')
    header = models.CharField(max_length=50)
    about_info = models.TextField(max_length=8000, verbose_name='Текст')
    def __str__(self):
        return '(%s)-%s' % (self.header,self.about_info)

