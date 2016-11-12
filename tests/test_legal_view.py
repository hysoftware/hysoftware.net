#!/usr/bin/env python
# coding=utf-8

"""Legal view tests."""

from django.test import TestCase
from .view_base import TemplateViewTestBase
from app.legal.views import LegalView, CSSView


class LegalViewTest(TemplateViewTestBase, TestCase):
    """Legal view access test."""

    template_name = "legal.html"
    endpoint = "legal:index"
    page_url = "/l/"
    view_cls = LegalView


class CSSViewTest(TemplateViewTestBase, TestCase):
    """CSS view access test."""

    template_name = "legal.css"
    endpoint = "legal:css"
    page_url = "/l/css"
    view_cls = CSSView
    content_type = "text/css"
