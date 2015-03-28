# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_remove_pendingverification_token'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VerifiedEmails',
            new_name='VerifiedEmail',
        ),
    ]
