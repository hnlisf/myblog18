#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category,Tag,Post

# Register your models here.

# 定制post的后台显示
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)


