# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 08:12
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20161107_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='github_user_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, null=True),
        ),
    ]
