#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-

from django import forms
from .models import Post

# 定义发布文章的表单类
class PubForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','excerpt','category','tags','img',]