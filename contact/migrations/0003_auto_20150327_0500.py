# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0020_auto_20150327_0205'),
        ('contact', '0002_auto_20150213_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingverification',
            name='assignee',
            field=models.ForeignKey(to='about.Developer', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verifiedemails',
            name='assignee',
            field=models.ForeignKey(to='about.Developer', default=''),
            preserve_default=False,
        ),
    ]
