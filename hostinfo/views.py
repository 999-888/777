#! coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.template.context import RequestContext
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .addinfo import AddData
from .models import Host
from .getinfo import Tom,GetLog,AnyCommand
import json
def index(req):
	if AddData():
		contacts=Host.objects.all()
		return render(req,'hostinfo/index.html',{'contacts':contacts})
	else:	
		return HttpResponse(u'获取信息失败')
def Actions(req,pk):
	h=Host.objects.get(id=pk)
	print("actions-h:%s"%h.name)
	return render(req,'hostinfo/actions.html',{'h':h})
def TomLog(req,ip):
	data=GetLog(ip)
	print(data)
	return render(req,'hostinfo/tomlog.html',{'data':data})
def TomRe(req,ip):
	data=Tom(ip)
	return render(req,'hostinfo/tomre.html',{'data':data})	
def login(req):
	if req.method == 'GET':
		form=LoginForm()
		return render_to_response('hostinfo/login.html',RequestContext(req,{'form':form}))
	else:
		form=LoginForm(req.POST)
		if form.is_valid():
			username=req.POST.get('username','')
			password=req.POST.get('password','')
			user=auth.authenticate(username=username,password=password)
			if user is not None and user.is_active:
				auth.login(req,user)
				#return render_to_response('index.html',RequestContext(req))
				return HttpResponseRedirect("hostinfo/")
			else:
				return render_to_response('hostinfo/login.html',RequestContext(req,{'form':form,'password_is_wrong':True}))
		else:
			return render_to_response('hostinfo/login.html',RequestContext(req,{'form':form}))
def logout(req):
	auth.logout(req)  
        return HttpResponseRedirect("/")
def listp(req):
	if AddData():
		contact_list=Host.objects.all()
		paginator = Paginator(contact_list,15)
		page=req.GET.get('page')
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts=paginator.page(1)
		except EamptyPage:
			contacts = paginator.page(paginator.num_pages)
		return render(req,'hostinfo/index.html',{'contacts':contacts})
	else:
		return HttpResponse(u'获取信息失败')
def Command(req):
	ip=req.GET['ip']
	print('ip:%s'%ip)
	command=req.GET['command']
	print('command:%s'%command)
	data=AnyComand(ip,command)
	print(data)
	data=json.dumps(data)
	return render(req,'hostinfo/actions.html',{'data':data})
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))
