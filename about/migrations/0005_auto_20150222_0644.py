# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20150222_0600'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NatualLanguages',
            new_name='NaturalLanguages',
        ),
        migrations.AddField(
            model_name='externalwebsite',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, db_index=True),
            preserve_default=True,
        ),
    ]
