#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import pubphoto,ShowPhotoView,likes

app_name='photo'

urlpatterns=[
    url(r'^pub/(?P<user_pk>\d+)/$',pubphoto,name='pub'),
    url(r'^show/$',ShowPhotoView.as_view(),name='show'),
    url(r'^show/likes/(?P<photo_pk>\d+)/$',likes,name='likes')
]
