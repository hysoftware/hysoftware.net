#!/usr/bin/env python
# coding=utf-8

"""Common view tests."""

from unittest.mock import patch
from django.test import TestCase, RequestFactory

from app.common.views import JSView, CSSView, ImageView
from app.common.models import ThirdPartyAssets

from .view_base import TemplateViewTestBase, URLAssignmentTestBase


class JSViewTest(TemplateViewTestBase, TestCase):
    """JSView Test."""

    endpoint = "common:js"
    content_type = "application/javascript"
    template_name = "common.js"
    page_url = "/c/js"
    view_cls = JSView


class CSSViewTest(TemplateViewTestBase, TestCase):
    """CSSView Test."""

    endpoint = "common:css"
    content_type = "text/css"
    template_name = "common.css"
    page_url = "/c/css"
    view_cls = CSSView


class AssetTest(URLAssignmentTestBase, TestCase):
    """Third party asset access test."""

    page_url = "/c/assets/test"
    endpoint = "common:assets"
    view_cls = ImageView
    url_kwargs = {"filename": "test"}

    def setUp(self, *args, **kwargs):
        """Setup."""
        self.request = RequestFactory().get(self.page_url)

    @patch("app.common.views.get_object_or_404")
    def test_get(self, objects):
        """The content should be rendered."""
        objects.return_value.image.read.return_value = "Test"
        result = self.view(self.request, filename="test")
        objects.assert_called_once_with(ThirdPartyAssets, filename="test")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result["Content-Type"], "image/jpeg")
        self.assertEqual(
            result.content.decode("utf-8"),
            objects.return_value.image.read.return_value
        )
