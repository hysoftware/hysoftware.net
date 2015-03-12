# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_jobtable_agent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='xero_key',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='xero_secret',
        ),
    ]
