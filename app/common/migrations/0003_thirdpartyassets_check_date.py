# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20161107_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdpartyassets',
            name='check_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]