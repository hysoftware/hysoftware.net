#!/usr/bin/env python
# coding=utf-8

"""Legal view tests."""

from unittest.mock import patch

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from .view_base import TemplateViewTestBase

from app.legal.views import LegalView


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
        self.assertEqual(
            view.assets_info, [
                {
                  "name": _("Homepage Title Background"),
                  "page": reverse("home:index"),
                  "license": "CC0",
                  "source": "http://alana.io/downloads/apple-macbook-laptop/",
                  "license_url": "http://alana.io/license/",
                  "check_date": "2017-07-18"
                }, {
                  "name": _("Legal Page Title Background"),
                  "page": reverse("legal:index"),
                  "license": "CC0",
                  "source": "http://alana.io/downloads/book-3/",
                  "license_url": "http://alana.io/license/",
                  "check_date": "2017-07-18"
                }, {
                  "name": _("About Page Title Background"),
                  "page": reverse("user:about"),
                  "license": "CC0",
                  "source": "http://alana.io/downloads/menu-2",
                  "license_url": "http://alana.io/license/",
                  "check_date": "2017-07-18"
                }, {
                  "name": _("Contact Page Title Background"),
                  "page": reverse("user:contact"),
                  "license": "CC0",
                  "source": "http://alana.io/downloads/iphone/",
                  "license_url": "http://alana.io/license/",
                  "check_date": "2017-07-18"
                }
            ]
        )

    def test_desc(self):
        """The description should be 'Legal Statement'."""
        self.assertEqual(self.view_cls.description, "Legal Statement")
