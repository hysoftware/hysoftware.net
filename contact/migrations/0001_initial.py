# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PendingVerification',
            fields=[
                ('email', models.CharField(primary_key=True, max_length=40, serialize=False)),
                ('token', models.CharField(max_length=40)),
                ('expires', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VerifiedEmails',
            fields=[
                ('email', models.CharField(primary_key=True, max_length=40, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
