"""
WSGI config for hysoft project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import cbsettings

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_FACTORY", "app.settings.devel.DevelConfig"
)
cbsettings.configure()

application = get_wsgi_application()
