# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20161124_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='title',
            field=models.CharField(db_index=True, default='Software Engineer', max_length=40),
            preserve_default=False,
        ),
    ]
