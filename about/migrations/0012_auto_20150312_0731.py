# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_auto_20150312_0341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='externalwebsite',
            old_name='choice',
            new_name='website_type',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
    ]
