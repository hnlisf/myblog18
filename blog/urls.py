#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import IndexView,PostDetailView,ArchivesView,CategoryView,TagsView,post_pub



app_name='blog'

urlpatterns=[
    url('^$',IndexView.as_view(),name='index'),
    url('^post/(?P<pk>\d+)/$',PostDetailView.as_view(),name='detail'),
    url('^archives/(?P<year>\d{4})/(?P<month>\d{1,2})/$',ArchivesView.as_view(),name='archives'),
    url('^category/(?P<pk>\d+)/$',CategoryView.as_view(),name='category'),
    url('^tags/(?P<pk>\d+)/$',TagsView.as_view(),name='tags'),
    url('^pubpost/(?P<user_pk>\d+)/$',post_pub,name='pubpost'),

]