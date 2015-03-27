# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20150327_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendingverification',
            name='token',
        ),
    ]
