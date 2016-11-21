#!/usr/bin/env python
# coding=utf-8

"""User view tests."""

from django.test import TestCase
from .view_base import TemplateViewTestBase
from app.user.views import AboutView


class AboutPageTest(TemplateViewTestBase, TestCase):
    """About page test."""

    endpoint = "user:about"
    page_url = "/u/about"
    view_cls = AboutView
    template_name = "about.html"
