#!/usr/bin/env python
# coding=utf-8

"""Test home view."""

from unittest.mock import patch
from django.http import HttpResponse
from django.test import TestCase, RequestFactory

from app.home.views import HomeView


class HomeViewRenderingTest(TestCase):
    """Home View Rendering Test."""

    def setUp(self):
        """Setup."""
        self.request = RequestFactory().get("/")
        self.view = HomeView.as_view()

    @patch("django.shortcuts.render", return_value=HttpResponse("ok."))
    def test_home_access(self, render):
        """Accessing /, home template should be rendered."""
        result = self.view(self.request)
        self.assertEqual(render.return_value.content, result.content)
        self.assertEqual(render.return_value.status_code, result.status_code)

    @patch("django.shortcuts.render", return_value=HttpResponse("ok."))
    def test_render_call(self, render):
        """Accessing /, render should be called once with proper params."""
        self.view(self.request)
        render.assert_called_once_with("home.html")
