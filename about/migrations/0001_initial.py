# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40, serialize=False, primary_key=True)),
                ('xero_key', models.CharField(max_length=40)),
                ('xero_secret', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
