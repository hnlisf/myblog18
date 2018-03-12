#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginname', models.CharField(db_index=True, max_length=64, unique=True)),
                ('Fullname', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('url_height', models.PositiveIntegerField(default=36)),
                ('url_width', models.PositiveIntegerField(default=36)),
                ('headshot', models.ImageField(height_field=models.PositiveIntegerField(default=36), upload_to='avatar/headshot/%Y/%m/%d/', width_field=models.PositiveIntegerField(default=36))),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created_time', models.DateField(auto_now_add=True)),
                ('modified_time', models.DateField(auto_now=True)),
                ('excerpt', models.CharField(blank=True, max_length=200)),
                ('url_height', models.PositiveIntegerField(default=340)),
                ('url_width', models.PositiveIntegerField(default=840)),
                ('img', models.ImageField(height_field=models.PositiveIntegerField(default=340), upload_to='avatar/post/%Y/%m/%d/', width_field=models.PositiveIntegerField(default=840))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogUser')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
