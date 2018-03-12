#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-

# RSS 功能模块

from django.contrib.syndication.views import Feed
from .models import Post

class AllPostRssFeed(Feed):

    # 显示在聚合阅读器上的标题
    title = 'tangx blog'

    # 通过聚合阅读器跳转到网址的地址

    link = '/index/'

    # 显示在聚合阅读器上的描述信息

    description = 'tangx的技术,生活，感悟分享'

    # 需要显示的内容条目

    def items(self):
        return Post.objects.all()

    # 聚合器中显示的内容条目的标题

    def item_title(self, item):
        return '[%s]%s'%(item.category,item.title)

    # 聚合器中显示的内容条目的描述

    def item_description(self, item):
        return item.body
