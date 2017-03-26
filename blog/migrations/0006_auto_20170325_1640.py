# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170325_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(max_length=500, null=True, unique=True),
        ),
    ]
