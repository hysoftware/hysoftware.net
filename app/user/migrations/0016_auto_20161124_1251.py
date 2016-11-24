# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_userinfo_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='angel_co',
            field=models.CharField(blank=True, db_index=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='github',
            field=models.CharField(max_length=39, unique=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='hacker_rank',
            field=models.CharField(blank=True, db_index=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='linkedin',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
