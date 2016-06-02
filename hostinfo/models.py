#! coding=utf-8
from __future__ import unicode_literals

from django.db import models

class Host(models.Model):
	name=models.CharField('主机名',max_length=50)
	ip=models.CharField('IP地址',max_length=50)
	kn=models.CharField('内核版本',max_length=50)
	release=models.CharField('centos版本',max_length=50)
	disk=models.CharField('磁盘空间总量',max_length=50)
	mem=models.CharField('内存总量',max_length=50)
	
	def __str__(self):
		return (self.name,self.ip)
	class Meta:
		verbose_name='服务器'
		verbose_name_plural='服务器'
class HostIp(models.Model):
	addr=models.CharField('IP地址',max_length=50)
	def __str__(self):
		return self.addr
	class Meta:
		verbose_name='服务器IP'
		verbose_name_plural='服务器IP'
