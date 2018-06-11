#!/usr/bin/env python
# coding=utf-8

"""Test home view."""

from django.test import TestCase
# from django.urls import reverse

from app.home.views import HomeView, SSLValidationView

from .view_base import TemplateViewTestBase


class HomeViewRenderingTest(TemplateViewTestBase, TestCase):
    """Home View Rendering Test."""

    template_name = "home.html"
    endpoint = "home:index"
    page_url = "/"
    view_cls = HomeView


class SSLValidationTextTest(TemplateViewTestBase, TestCase):
    """SSL Validation text test."""

    template_name = "A19129EBDFBB9D747449765BAEB1C234.txt"
    content_type = "text/plain"
    view_cls = SSLValidationView
    endpoint = "home:ssl"
    page_url = "/A19129EBDFBB9D747449765BAEB1C234.txt"
