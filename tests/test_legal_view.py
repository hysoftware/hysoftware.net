#!/usr/bin/env python
# coding=utf-8

"""Legal view tests."""

from unittest.mock import patch

from django.test import TestCase
from .view_base import TemplateViewTestBase

from app.legal.views import LegalView, CSSView, JSView


class LegalViewTest(TemplateViewTestBase, TestCase):
    """Legal view access test."""

    template_name = "legal.html"
    endpoint = "legal:index"
    page_url = "/l/"
    view_cls = LegalView

    @patch("app.legal.models.RecognizedCountry.objects")
    def test_recognized_country(self, objects):
        """Test recognized country class."""
        view = self.view_cls()
        self.assertIs(view.country, objects)

    @patch("app.user.models.UserInfo.objects")
    def test_user_info(self, objects):
        """Test recognized country class."""
        view = self.view_cls()
        self.assertIs(view.users_info, objects)

    @patch("app.common.models.ThirdPartyAssets.objects")
    def test_third_party_asset_info(self, objects):
        """Test Third Party Asset information fetch."""
        view = self.view_cls()
        self.assertIs(view.assets_info, objects)


class CSSViewTest(TemplateViewTestBase, TestCase):
    """CSS view access test."""

    template_name = "legal.css"
    endpoint = "legal:css"
    page_url = "/l/css"
    view_cls = CSSView
    content_type = "text/css"


class JSViewTest(TemplateViewTestBase, TestCase):
    """JS view access test."""

    template_name = "legal.js"
    endpoint = "legal:js"
    page_url = "/l/js"
    view_cls = JSView
    content_type = "application/javascript"
