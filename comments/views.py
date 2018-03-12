#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm
from users.models import User

# Create your views here.
# 发布评论的视图函数
def post_comment(request,post_pk,user_pk):
    # 获得当前文章对象，登录的用户对象
    post=get_object_or_404(Post,pk=post_pk)
    user=get_object_or_404(User,pk=user_pk)
    # 如果为post方法
    if request.method=='POST':
        form=CommentForm(request.POST)
        # 如果表单内容合规
        if form.is_valid():
            # 创建评论对象，不保存到数据库
            comment=form.save(commit=False)

            comment.post=post
            comment.user=user

            # 保存评论表单数据到数据库,重定向当前页
            comment.save()
            return redirect(post)
        else:
            # 获得当前所有评论列表
            comment_list=post.comment_set.all()
            # 将当前页面表单内容，文章，评论列表保存后，重新渲染页面
            context={
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)
    else:
        # get访问时，刷新页面
        return redirect(post)