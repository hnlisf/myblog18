#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from users.models import User

# Create your models here.
class MyPhoto(models.Model):
    title=models.CharField(max_length=60,verbose_name='标题')
    upload_time=models.DateTimeField(auto_now_add=True,verbose_name='上传时间')
    description=models.CharField(max_length=300,verbose_name='描述')
    photo=models.ImageField(upload_to='avatar/myphoto/%Y/%m/%d/')
    photo_author=models.ForeignKey(User,verbose_name='作者')
    views=models.PositiveIntegerField(verbose_name='点赞量',default=0)

    def __str__(self):
        return self.title

