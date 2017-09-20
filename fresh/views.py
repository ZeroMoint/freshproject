from django.shortcuts import render, redirect
from hashlib import sha1
from .models import *
from django.http import HttpResponseRedirect


def register(request):
	return render(request,'fresh/register.html')

def login(request):
	uname=request.COOKIES.get('uname','')
	context={'title':'用户登录','error_name':0,'uname':uname}
	return render(request,'fresh/login.html',context)

def login_handle(request):
	post=request.POST
	uname=post.get('username')
	upwd=post.get('pwd')
	jizhu=post.get('jizhu',0)
	user=UserInfo.objects.filter(uname=uname)
	if len(user)==1:
		upwd=upwd.encode('utf-8')
		s1=sha1(upwd)
		if s1.hexdigest()==user[0].upwd:
			red=HttpResponseRedirect('/user/info/')
			if jizhu==0:
				red.set_cookie('uname',uname)
			else:
				red.set_cookie('uname','',max_age=-1)
			request.session['user_id']=user[0].id
			request.session['user_name']=uname
			return red
		else:
			context={'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
			return render(request,'fresh/login.html',context)
	else:
		context={'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
		return render(request,'fresh/login.html',context)

def register_handle(request):
	#接受用户输入
	post=request.POST
	uname=post.get('user_name')
	upwd=post.get('pwd')
	upwd2=post.get('cpwd')
	uemail=post.get('email')
	#判断两次密码
	if upwd!=upwd2:
		return redirect('/user/register/')
	#密码加密
	upwd=upwd.encode('utf-8')
	s1=sha1(upwd)
	upwd3=s1.hexdigest()
	#创建对象
	user=UserInfo()
	user.uname=uname
	user.upwd=upwd3
	user.save()
	#注册成功，转到登录页面
	return redirect('/user/login/')

def register_exist(request):
	uname=request.GET.get('uname')
	count=UserInfo.objects.filter(uname=uname).count()
	return JsonResponse({'count':count})

def info(request):
	return render(request,'fresh/user_center_info.html')

def order(request):
	return render(request,'fresh/user_center_order.html')

def site(request):
	user=UserInfo.objects.get(id=request.session['user_id'])
	if request.method == 'POST':
		post=request.POST
		user.ushou=post.get('ushou')
		user.uaddress=post.get('uaddress')
		user.uyoubian=post.get('uyoubian')
		user.uphone=post.get('uphone')
		user.save()
	context={'title':'用户中心','user':user}

	return render(request,'fresh/user_center_site.html',context)
	

