# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20150222_0644'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Developers',
            new_name='Developer',
        ),
        migrations.RenameModel(
            old_name='ProgrammingLanguages',
            new_name='NaturalLanguage',
        ),
        migrations.RenameModel(
            old_name='Occupations',
            new_name='Occupation',
        ),
        migrations.RenameModel(
            old_name='NaturalLanguages',
            new_name='ProgrammingLanguage',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
