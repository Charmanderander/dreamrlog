# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 07:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nineku', '0011_auto_20151225_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dreamdb',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 25, 15, 47, 54, 642906)),
        ),
        migrations.AlterField(
            model_name='likes',
            name='postid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
