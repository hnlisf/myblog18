#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.auth.models import User
from django.utils.html import strip_tags

from myblog.settings import MEDIA_ROOT
from users.models import User
from django.urls import reverse
import markdown

# Create your models here.
# 分类
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# #定义上传文章图片的方法
# def postimg_upload(instance,filename):
#     return "/".join([MEDIA_ROOT, instance.tilte,filename])


# 文章
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    # 摘要
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag')

    # 作者
    author = models.ForeignKey(User)

    # 阅读量
    views = models.PositiveIntegerField(default=0)

   # 文章图片
   #  url_height = models.PositiveIntegerField(default=340)
   #  url_width = models.PositiveIntegerField(default=840)
    img = models.ImageField(upload_to='avatar/post/%Y/%m/%d/',default='post.jpg')

    # 定义默认的排序方法,以发布时间倒序排列
    class Meta:
        ordering=['-created_time']

    def __str__(self):
        return self.title

    # 获取文章post的绝对url
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    # 获得文章阅读量的方法
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 获得自动文章摘要的方法
    def save(self,*args,**kwargs):
        if not self.excerpt:
            md=markdown.Markdown(
                extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                ]
            )
            self.excerpt=strip_tags(md.convert(self.body))[:66]

        super().save(*args,**kwargs)






