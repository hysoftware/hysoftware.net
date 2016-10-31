#!/usr/bin/env python
# coding=utf-8

"""Check URL existence functionality test."""

from unittest.mock import patch
from django.test import TestCase
from django.urls import NoReverseMatch

from app.jinja_env import url_exists


class ReverseCallTest(TestCase):
    """url_exists calls reverse function."""

    @patch("app.jinja_env.reverse", return_value="ok")
    def test_reverse_call(self, reverse):
        """Reverse should be called and the return value should be True."""
        result = url_exists("test")
        reverse.assert_called_once_with("test")
        self.assertIs(result, True)

    @patch("app.jinja_env.reverse", side_effect=NoReverseMatch)
    def test_exception(self, reverse):
        """Function url_exists should return False."""
        self.assertIs(url_exists("test"), False)
