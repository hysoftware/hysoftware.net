# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0020_auto_20150327_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtable',
            name='website_type',
            field=models.CharField(choices=[('UP', 'upwork'), ('EL', 'Elance'), ('DR', 'Direct Contract')], max_length=4, db_index=True),
        ),
    ]
