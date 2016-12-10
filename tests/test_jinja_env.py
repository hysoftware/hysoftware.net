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

    def test_reverse(self):
        """The options should have 'url' funciton."""
        from django.core.urlresolvers import reverse
        self.assertDictContainsSubset({
            "url": reverse
        }, self.options.globals)

    def test_resolve(self):
        """The options should have 'resolve' function."""
        from django.core.urlresolvers import resolve
        from app.jinja_env import url_exists
        self.assertDictContainsSubset(
            {"resolve": resolve, "url_exists": url_exists},
            self.options.globals
        )

    def test_translation(self):
        """The options should have translation functions."""
        from django.utils.translation import ugettext, ungettext
        self.assertDictContainsSubset({
            "_": ugettext, "_n": ungettext
        }, self.options.globals)

    def test_settings(self):
        """The optoins should have settings as global variable."""
        from django.conf import settings
        self.assertDictContainsSubset({
            "settings": settings
        }, self.options.globals)

    def test_getattr(self):
        """The option should have getattr as global variable."""
        self.assertDictContainsSubset({
            "getattr": getattr
        }, self.options.globals)

    def test_md(self):
        """The options should have markdown compiler as filter."""
        from markdown import markdown
        self.assertDictContainsSubset({
            "markdown": markdown
        }, self.options.filters)

    def test_urlparse(self):
        """The options should have urlparse function as global variable."""
        from urllib.parse import urlparse
        self.assertDictContainsSubset({
            "urlparse": urlparse
        }, self.options.globals)
