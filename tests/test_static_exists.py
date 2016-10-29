#!/usr/bin/env python
# coding=utf-8

"""Static file exist check tests."""

from unittest.mock import patch
from django.test import TestCase
from app.jinja_env import __static_exists__


class StaticExistsCallTest(TestCase):
    """Static exitsts function call test."""

    @patch("app.jinja_env.find")
    def test_find_call(self, find):
        """Find static function should be called."""
        __static_exists__("test")
        find.assert_called_once_with("test", all=True)
