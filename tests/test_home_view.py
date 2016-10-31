#!/usr/bin/env python
# coding=utf-8

"""Test home view."""

from unittest.mock import patch
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.test import TestCase, RequestFactory

from app.home.views import HomeView


class HomeViewRenderingTest(TestCase):
    """Home View Rendering Test."""

    def setUp(self):
        """Setup."""
        self.request = RequestFactory().get("/")
        self.view = HomeView.as_view()

    def test_utl(self):
        """The url should be /."""
        self.assertEqual(reverse("home:index"), "/")

    def test_home_template(self):
        """Home view should have proper template."""
        self.assertEqual(HomeView.template_name, "home.html")

    @patch("app.home.views.HomeView.get", return_value=HttpResponse("ok"))
    def test_render_call(self, get):
        """Accessing /, render should be called once with proper params."""
        self.view(self.request)
        get.assert_called_once_with(self.request)
