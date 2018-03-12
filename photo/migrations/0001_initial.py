#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 04:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='myphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='标题')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('description', models.CharField(max_length=300, verbose_name='描述')),
                ('photo', models.ImageField(upload_to='')),
                ('views', models.PositiveIntegerField(verbose_name='阅读量')),
                ('photo_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
    ]
