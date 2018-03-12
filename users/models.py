#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



# # 定义用户头像上传的文件路径
# def headimg_upload(instance,filename):
#         return "/".join([MEDIA_ROOT, instance.loginname,filename])

# 定义用户模型,继承AbstractUser
class User(AbstractUser):
    nickname = models.CharField(max_length=64,unique=True,db_index=True,verbose_name='昵称')
    signature = models.CharField(max_length=128,default='这家伙很懒什么都没有留下',verbose_name='个性签名')

    # url_height = models.PositiveIntegerField(default=36)
    # url_width = models.PositiveIntegerField(default=36)
    # 自动获取头像的大小,放入url_height/url_width
    headshot = models.ImageField(upload_to='avatar/headshot/%Y/%m/%d/', default='default.jpg',verbose_name='头像')

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.username
