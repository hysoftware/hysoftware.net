#!/usr/bin/env python

"""
WSGI config for hysoft project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import requests
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from uwsgidecorators import timer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hysoft.settings")
# pylint: disable=invalid-name
application = DjangoWhiteNoise(get_wsgi_application())


# 1800 secs = 30 minutes
@timer(1800)
def ping():
    '''
    According to heroku document (See below), single dyno sleeps when
    there is no action in 1 hour. This ping function prevents this sleep:
    https://devcenter.heroku.com/articles/dynos#dyno-sleeping
    '''
    destination = os.environ.get("PING_DEST", "http://localhost:50000/")
    requests.get(destination)
