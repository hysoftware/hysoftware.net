# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0016_auto_20150326_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalwebsite',
            name='website_type',
            field=models.CharField(db_index=True, choices=[('G+', 'Google Plus'), ('LI', 'Linkedin'), ('FB', 'Facebook'), ('TW', 'Twitter'), ('CW', 'Coderwalll'), ('AS', 'Assembly'), ('GH', 'Github'), ('BB', 'Bitbucket'), ('OT', 'Other')], max_length=4),
            preserve_default=True,
        ),
    ]
