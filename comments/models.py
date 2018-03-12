#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from users.models import User
from blog.models import Post

# Create your models here.
# 评论模型
class Comment(models.Model):
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User)
    post=models.ForeignKey(Post)

    def __str__(self):
        return self.text[:20]
