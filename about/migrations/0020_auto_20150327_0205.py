# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0019_auto_20150326_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='externalwebsite',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='jobtable',
            old_name='agent',
            new_name='website_type',
        ),
    ]
