# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developers',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='developers',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
