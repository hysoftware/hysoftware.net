#!/usr/bin/env python
# coding=utf-8

"""Common view tests."""

from django.test import TestCase

from app.common.views import JSView, CSSView

from .view_base import TemplateViewTestBase


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
