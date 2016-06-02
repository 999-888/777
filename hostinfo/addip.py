#! coding=utf-8
'''
获取指定excel表格第一列的IP信息，生成一个列表并返回结果列表
'''
import xlrd
import sys,os
from .models import HostIp
def GetIp(File):
	try:
		bk=xlrd.open_workbook(File)
		tb=bk.sheet_by_index(0)
	except Exception as e:
		print(e)
		return 0
	data1=tb.col_values(0)
	return data1
def AddIp():
	FILE='./hostinfo/upfile/ip.xlsx'
	IPS=GetIp(FILE)
	print(IPS)
	for ip in IPS:
		HostIp.objects.get_or_create(addr=ip)
	
	return 1

