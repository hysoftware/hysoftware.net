# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20150328_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingverification',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
