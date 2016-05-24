#!/usr/bin/env python
# coding=utf-8

"""HTML Minification Tests."""

from unittest import TestCase
from unittest.mock import patch

from app.common import minify_html


class TestHTMLMinification(TestCase):
    """HTML Minification test."""

    @patch("htmlmin.minify")
    def test_html_minificaton(self, minify_mock):
        """htmlmin.minify should be called with proper kwargs."""
        test = "This is a test"
        minify_html(test)
        minify_mock.assert_called_once_with(
            test,
            remove_comments=True,
            remove_empty_space=True,
            remove_optional_attribute_quotes=False
        )
