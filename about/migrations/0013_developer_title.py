# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0012_auto_20150312_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='title',
            field=models.CharField(default='', db_index=True, max_length=40),
            preserve_default=False,
        ),
    ]
