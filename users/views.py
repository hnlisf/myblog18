#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm
from django.urls import reverse

# Create your views here.

# 用户注册的方法
def register(request):
    redirect_to=request.POST.get('next',request.GET.get('next',''))
    # 如果为POST方法
    if request.method=='POST':
        # 生成表单对象
        form=RegisterForm(request.POST,request.FILES)
        # 如果表单输入合法
        if form.is_valid():
            # 保存表单
            form.save()
            if redirect_to:
                return redirect(redirect_to)

            return redirect(reverse('blog:index'))
    else: # 如果为get方法
            form=RegisterForm()
    # 将表单返回注册页面
    return render(request,'users/register.html',{'form':form,'next':redirect_to})

