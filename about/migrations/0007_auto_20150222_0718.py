# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20150222_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupation',
            name='description',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='occupation',
            name='end_year',
            field=models.DateField(default=datetime.datetime(2015, 2, 22, 7, 18, 21, 340500, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupation',
            name='start_year',
            field=models.DateField(default=datetime.datetime(2015, 2, 22, 7, 18, 31, 884374, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupation',
            name='where',
            field=models.CharField(max_length=100, db_index=True, default=''),
            preserve_default=False,
        ),
    ]
