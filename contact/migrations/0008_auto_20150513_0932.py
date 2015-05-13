# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20150331_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingverification',
            name='token_hash',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
