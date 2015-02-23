# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20150222_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupation',
            name='end_year',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='occupation',
            name='start_year',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
