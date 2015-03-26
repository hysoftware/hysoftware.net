# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0017_auto_20150326_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtable',
            name='agent',
            field=models.CharField(db_index=True, max_length=4, choices=[('OD', 'oDesk'), ('EL', 'Elance'), ('DR', 'Direct Contract')]),
            preserve_default=True,
        ),
    ]
