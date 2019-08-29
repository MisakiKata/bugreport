from django.db import models

# Create your models here.


"""应用列表"""


class appname(models.Model):
    name = models.CharField(verbose_name='应用名称', max_length=30)
    abbrename = models.CharField(verbose_name='应用简称', max_length=30)
    developuser = models.CharField(verbose_name='开发人员', max_length=30)
    researchuser = models.CharField(verbose_name='研发负责人', max_length=30)
    appurl = models.URLField(verbose_name='应用地址')

    class Meta:
        verbose_name = '应用管理'
        verbose_name_plural = '应用管理'

    def __str__(self):
        return self.name

