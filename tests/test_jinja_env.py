#!/usr/bin/env python
# coding=utf-8

"""Jinja Environment Dict Test."""

from django.test import TestCase
from app.jinja_env import jinja_options


class DictTest(TestCase):
    """The env should have propert global variables and filters."""

    def setUp(self):
        """Setup."""
        self.options = jinja_options()

    def test_static_file(self):
        """The options should have static file reoslver."""
        from django.contrib.staticfiles.storage import staticfiles_storage
        from app.jinja_env import __static_exists__
        self.assertDictContainsSubset({
            "static": staticfiles_storage.url,
            "static_exists": __static_exists__
        }, self.options.globals)
