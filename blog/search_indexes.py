#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-

from haystack import indexes
from .models import Post

# 全文检索模块
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        print(self.get_model().objects.all())
        return self.get_model().objects.all()