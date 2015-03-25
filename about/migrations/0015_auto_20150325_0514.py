# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_auto_20150324_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalwebsite',
            name='website_type',
            field=models.CharField(choices=[('G+', 'Google Plus'), ('LI', 'Linkedin'), ('FB', 'Facebook'), ('TW', 'Twitter'), ('CW', 'Coderwalll'), ('AS', 'Assembly'), ('GH', 'Github'), ('BB', 'Bitbucket'), ('OT', 'Other')], db_index=True, max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jobtable',
            name='agent',
            field=models.CharField(choices=[('OD', 'oDesk'), ('EL', 'Elance'), ('DR', 'Direct Contract'), ('OT', 'Other')], db_index=True, max_length=4),
            preserve_default=True,
        ),
    ]
