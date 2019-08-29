from django.db import models
from datetime import datetime
# Create your models here.
from applist.models import appname
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

user = get_user_model()

"""漏洞列表"""


class vulnlist(models.Model):

    LEVEL = (
        (1, '高'),
        (2, '中'),
        (3, '低'),
    )

    STATUS = (
        (1, '新提交'),
        (2, '正在处理'),
        (3, '已修复，待验证'),
        (4, '修复完成'),
        (5, '已驳回'),
    )
    data_time = models.DateField(verbose_name='提交日期', default=datetime.now)
    title = models.CharField(verbose_name='漏洞标题', max_length=30)
    name = models.ForeignKey(appname, verbose_name='应用名称', max_length=30, null=True,on_delete=models.SET_NULL)
    developuser = models.ForeignKey(user, verbose_name='开发人员', max_length=30, null=True, on_delete=models.SET_NULL)
    level = models.IntegerField(verbose_name='漏洞等级', default=1, null=False, blank=False, choices=LEVEL)
    status = models.IntegerField(verbose_name='漏洞状态', default=1, null=False, blank=False, choices=STATUS)
    vulntext = RichTextUploadingField(verbose_name='漏洞详情')
    putuser = models.CharField(verbose_name='提交人', max_length=30, null=True)
    Repairplan = models.TextField(verbose_name='修复方案', default='')


    class Meta:
        verbose_name = '漏洞提交'
        verbose_name_plural = '漏洞提交'


    def __str__(self):
        return self.title


class trace_esc(models.Model):

    data = models.CharField(verbose_name='用户进度', max_length=100, default='')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    vulnid = models.CharField(verbose_name='漏洞ID', max_length=50, default='')
    developuser = models.CharField(verbose_name='开发人员', max_length=100, default='')