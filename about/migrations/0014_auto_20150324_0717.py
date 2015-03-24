# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_developer_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Occupation',
        ),
    ]
