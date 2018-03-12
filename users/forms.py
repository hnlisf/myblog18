#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from .models import User

# 创建用户注册的表单
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields = ['username','email','nickname','headshot','signature']