# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20150221_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=4, db_index=True, choices=[('G+', 'Google Plus'), ('LI', 'Linkedin'), ('FB', 'Facebook'), ('TW', 'Twitter'), ('CW', 'Coderwalll'), ('GH', 'Github'), ('BB', 'Bitbucket')])),
                ('url', models.URLField()),
                ('user', models.ForeignKey(to='about.Developer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, db_index=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('user', models.ForeignKey(to='about.Developer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NatualLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=40, db_index=True)),
                ('user', models.ForeignKey(to='about.Developer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=30, db_index=True)),
                ('user', models.ForeignKey(to='about.Developer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgrammingLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=40, db_index=True)),
                ('user', models.ForeignKey(to='about.Developer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20, db_index=True)),
                ('user', models.ForeignKey(to='about.Developer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='developer',
            name='first_name',
            field=models.CharField(max_length=20, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='developer',
            name='last_name',
            field=models.CharField(max_length=20, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='developer',
            name='xero_key',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='developer',
            name='xero_secret',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
    ]
