# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20150222_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtable',
            name='agent',
            field=models.CharField(max_length=4, default='OT', db_index=True, choices=[('OD', 'oDesk'), ('EL', 'Elance'), ('AS', 'Assembly'), ('OT', 'Other')]),
            preserve_default=False,
        ),
    ]
