# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-21 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0005_auto_20171212_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=400, verbose_name='\u95ee\u9898'),
        ),
    ]
