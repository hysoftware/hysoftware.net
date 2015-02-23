# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_auto_20150222_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupation',
            name='end_year',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
