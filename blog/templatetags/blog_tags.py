#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django import template
from django.db.models import Count

from ..models import Post,Category,Tag
from comments.models import Comment

register=template.Library()

# 最新文章模版标签
@register.simple_tag
def get_recent_post(num=5):
    #默认获得最近的五篇文章
    return Post.objects.all().order_by('-created_time')[:num]

# 热门文章模板标签
@register.simple_tag
def get_hot_post(num=4):
    return Post.objects.annotate(num_comments=Count('comment')).order_by('-num_comments')[:num]

# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

# 分类模板标签
@register.simple_tag
def get_category():

    return Category.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)

# 标签云模板标签
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)
