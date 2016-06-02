#! coding=utf-8
import subprocess
hosts='/root/pb/hosts'

def GetData(Command):
	outdata=subprocess.Popen(Command,stdout=subprocess.PIPE,shell=True)
	try:
		outdata=outdata.stdout.readlines()[0].strip()
	except 	Exception as e:
		outdata=''
	return outdata

def GetName(IP):
	Command="ansible -i %s %s -m shell -a 'hostname' | grep -v rc" %(hosts,IP)
	outdata=GetData(Command)
	return outdata
def GetRelease(IP):
	Command="ansible -i %s %s -m shell -a 'cat /etc/redhat-release' | grep -v rc" %(hosts,IP)
	outdata=GetData(Command)
	return outdata
def GetKn(IP):
	Command="ansible -i %s %s -m shell -a 'uname -r' | grep -v rc" %(hosts,IP)
	outdata=GetData(Command)
	return outdata
def GetMem(IP):
	Command="ansible -i %s %s -m shell -a 'free -m' | grep Mem | awk '{print $2}'| grep -v rc"%(hosts,IP)
	outdata=GetData(Command)
	return outdata
def GetDisk(IP):
	Command="ansible -i %s %s -m shell -a 'fdisk -l' | grep 'sd' | grep 'Disk' | awk -F',' '{print $1}' |awk '{print $3 $4}'"%(hosts,IP)
	outdata=GetData(Command)
	return outdata
def GetLog(IP):
	Command="ansible -i %s %s -m shell -a 'tomcatd log 50' | grep -v  rc"%(hosts,IP)
	outdata=subprocess.Popen(Command,stdout=subprocess.PIPE,shell=True)
	outdata=outdata.stdout.readlines()
	return outdata
def Tom(IP):
	Command="ansible -i %s %s -m shell -a 'tomcatd restart'"%(hosts,IP)
	outdata=GetData(Command)
	return outdata
def PingTest(IP):
	Command="ansible -i %s %s -m ping | grep 'SUCCESS'"%(hosts,IP)
	outdata=GetData(Command)
	return outdata
def AnyCommand(IP,command):
	Command="ansible -i %s %s -m shell -a %s"%(hosts,IP,command)
	outdata=GetData(Command)
	return outdata
