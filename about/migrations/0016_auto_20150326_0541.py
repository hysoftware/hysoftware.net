# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0015_auto_20150325_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalwebsite',
            name='website_type',
            field=models.CharField(choices=[('gp', 'Google Plus'), ('li', 'Linkedin'), ('fb', 'Facebook'), ('tw', 'Twitter'), ('cw', 'Coderwalll'), ('as', 'Assembly'), ('gh', 'Github'), ('bb', 'Bitbucket'), ('ot', 'Other')], db_index=True, max_length=4),
            preserve_default=True,
        ),
    ]
