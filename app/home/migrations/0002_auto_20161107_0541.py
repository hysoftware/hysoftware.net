# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pitch',
            options={'verbose_name': 'Pitch', 'verbose_name_plural': 'Pitches'},
        ),
    ]