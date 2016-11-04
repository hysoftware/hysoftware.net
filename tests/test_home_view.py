#!/usr/bin/env python
# coding=utf-8

"""Test home view."""

from unittest.mock import patch
from django.test import TestCase

from app.common.models import ThirdPartyAssets
from app.home.views import HomeView, JSView, HomeTitleImageView

from .view_base import TemplateViewTestBase


class HomeViewRenderingTest(TemplateViewTestBase, TestCase):
    """Home View Rendering Test."""

    template_name = "home.html"
    endpoint = "home:index"
    page_url = "/"
    view_cls = HomeView


class HomeJSViewRenderingTest(TemplateViewTestBase, TestCase):
    """Home frontend script view rendering test."""

    template_name = "home.js"
    content_type = "application/javascript"
    endpoint = "home:js"
    page_url = "/js"
    view_cls = JSView


class HomeTitleImageRenderingTest(TestCase):
    """Home title image view tests."""

    def setUp(self):
        """Setup."""
        from django.test import RequestFactory
        self.request = RequestFactory().get("/title")
        self.view = HomeTitleImageView.as_view()

    @patch("app.home.views.get_object_or_404")
    def test_image_fetch(self, objects):
        """The image should be read."""
        objects.return_value.image.read.return_value = "Test"
        result = self.view(self.request)
        objects.assert_called_once_with(ThirdPartyAssets, filename="home")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result["Content-Type"], "image/jpeg"
        )
        self.assertEqual(
            result.content.decode("utf-8"),
            objects.return_value.image.read.return_value
        )
