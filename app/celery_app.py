#!/usr/bin/env python
# coding=utf-8

"""Celery app definition."""

import os
from celery import Celery
import cbsettings

os.environ.setdefault("DJANGO_SETTINGS_FACTORY", "app.settings.DevelConfig")
cbsettings.configure()

app = Celery(__name__)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
