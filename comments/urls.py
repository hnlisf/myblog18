#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import post_comment

app_name='comments'
urlpatterns=[
    url(r'^comments/post/(?P<post_pk>\d+)/(?P<user_pk>\d+)/$',post_comment,name='post_comment'),
]