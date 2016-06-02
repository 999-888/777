#! coding=utf-8
from .models import Host,HostIp
from .getinfo import *
from .addip import AddIp

def AddData():
	if AddIp():
		IPS=HostIp.objects.all()
		for ip in IPS:
			try:
				res=Host.objects.get(ip=ip)
			except Exception as e:
				print(' %s not found,now add it'%(ip))
				rr=PingTest(ip)
				print('PintTest:%s'%rr)
				if rr == '':
					continue
				else:
					try:
						r=GetRelease(ip)
						n=GetName(ip)
						k=GetKn(ip)
						m=GetMem(ip)
						d=GetDisk(ip)
						print('d:%s'%d)
						Host.objects.get_or_create(name=n,ip=ip,kn=k,release=r,mem=m,disk=d)
						print('%s done'%ip)
					except Exception as e:
						print('err:%s'%e)
	else:
		return 0
	return 1	
			
		
