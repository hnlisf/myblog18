#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from users.models import User
from .forms import PubPhotoForm
from django.views.generic import ListView

from .models import MyPhoto

# Create your views here.

# 发布图片
def pubphoto(request,user_pk):
   user = get_object_or_404(User,pk=user_pk)
   if request.method=='POST':
       form =  PubPhotoForm(request.POST,request.FILES)

       if form.is_valid():
           photo=form.save(commit=False)
           photo.photo_author=user
           photo.save()

           return redirect('/photo/show/')

       else:
           context={
               'form':form
           }
           return render(request,'photo/photopub.html',context=context)

   else:
       form=PubPhotoForm()
       return render(request,'photo/photopub.html',locals())

# def showphoto(request):
#     return render(request,'photo/show.html')

# 展示图片
class ShowPhotoView(ListView):
    model = MyPhoto
    template_name = 'photo/show.html'
    context_object_name = 'photo_list'

# 点赞的方法
def likes(request,photo_pk):
    myphoto=get_object_or_404(MyPhoto,pk=photo_pk)

    if request.method=='POST':
        myphoto.views+=1
        likes_num=myphoto.views
        myphoto.save()
        msg={'likesnum':likes_num}
        return  JsonResponse(msg)
    else:
        return redirect('/index/')



