# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20150222_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalwebsite',
            name='choice',
            field=models.CharField(max_length=4, choices=[('G+', 'Google Plus'), ('LI', 'Linkedin'), ('FB', 'Facebook'), ('TW', 'Twitter'), ('CW', 'Coderwalll'), ('GH', 'Github'), ('BB', 'Bitbucket'), ('OT', 'Other')], db_index=True),
            preserve_default=True,
        ),
    ]
