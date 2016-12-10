#!/usr/bin/env python
# coding=utf-8

"""Uwsgi tests."""

import sys
from unittest.mock import patch

from django.test import TestCase


class UWSGIApptest(TestCase):
    """UWSgiApp test."""

    def tearDown(self):
        """Unload the app."""
        del sys.modules["app.wsgi"]

    @patch("app.wsgi.get_wsgi_application")
    @patch("cbsettings.configure")
    @patch("os.environ.setdefault")
    def test_env(self, env_default, conf_func, app):
        """The DJANGO_SETTINGS_FACTORY should be devel conf by default."""
        import app.wsgi  # noqa
        env_default.assert_called_once_with(
            "DJANGO_SETTINGS_FACTORY", "app.settings.devel.DevelConfig"
        )

    @patch("app.wsgi.get_wsgi_application")
    @patch("cbsettings.configure")
    def test_configure(self, conf_func, app):
        """cbsettings.configure should be called."""
        import app.wsgi  # noqa
        conf_func.assert_called_once_with()

    @patch("django.core.wsgi.get_wsgi_application")
    @patch("cbsettings.configure")
    def test_app(self, conf_func, get_wsgi_application):
        """get_wsgi_application should be called."""
        from app.wsgi import application  # noqa
        get_wsgi_application.assert_called_once_with()
        self.assertIs(application, get_wsgi_application.return_value)
