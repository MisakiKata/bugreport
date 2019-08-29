from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
import time
# Create your models here.



"""用户列表"""


class Userlist(AbstractUser):
    email = models.EmailField(verbose_name='邮箱', unique=True)
    depart = models.CharField(verbose_name='所属部门', max_length=30, null=True, blank=True)
    telephone = models.CharField(verbose_name='联系电话', max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'

    def __str__(self):
        return self.username

class resetuser(models.Model):
    resettime = models.FloatField(verbose_name='重置时间', default='')
    resetuser = models.EmailField(verbose_name='重置邮箱', default='')
    resetcode = models.CharField(verbose_name='重置验证码', max_length=125)
    failtime = models.FloatField(verbose_name='失效时间', default='')
