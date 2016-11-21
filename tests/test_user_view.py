#!/usr/bin/env python
# coding=utf-8

"""User view tests."""

from unittest.mock import patch

from django.test import TestCase
from .view_base import TemplateViewTestBase
from app.user.views import AboutView, CSSView


class AboutPageTest(TemplateViewTestBase, TestCase):
    """About page test."""

    endpoint = "user:about"
    page_url = "/u/about"
    view_cls = AboutView
    template_name = "about.html"

    @patch("app.user.models.UserInfo.objects")
    def test_users_info_property(self, objects):
        """Users Info property should return the queryset of user info,"""
        self.assertIs(self.view_cls().users_info, objects)


class CSSPagetest(TemplateViewTestBase, TestCase):
    """CSS view test."""

    endpoint = "user:css"
    page_url = "/u/css"
    view_cls = CSSView
    template_name = "user.css"
    content_type = "text/css"
