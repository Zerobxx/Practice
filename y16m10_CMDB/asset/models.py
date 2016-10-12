#coding=utf-8

from django.db import models

# Create your models here.

class Asset(models.Model):
    asset_type_choices = (
        ('server', u'服务器'),
        ('switch', u'交换机'),
        ('firewall', u'防火墙'),
        ('others', u'其他类'),
    )

    asset_type = models.CharField(choices=asset_type_choices, max_length=64, default='server')
    name = models.CharField(max_length=64, unique=True)
    sn = models.CharField(u'资产SN编号', max_length=128, unique=True)
    manufactory = models.CharField(u'制造商', max_length=64, null = True, blank = True)
    management_ip = models.GenericIPAddressField(u'管理IP', blank = True, null = True)
    memo = models.TextField(u'备注', null = True, blank = True)

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = '资产总表'

    def __unicode__(self):
        return 'id:%s name:%s'  %(self.id, self.name)