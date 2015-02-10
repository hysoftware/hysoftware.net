# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pendingverification',
            old_name='email',
            new_name='email_hash',
        ),
        migrations.RenameField(
            model_name='verifiedemails',
            old_name='email',
            new_name='email_hash',
        ),
        migrations.AddField(
            model_name='pendingverification',
            name='message',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
