#!/home/blogenv/bin/python
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloguser',
            old_name='loginname',
            new_name='nickname',
        ),
    ]