#!/usr/bin/env python
# coding=utf-8

"""Test home view."""

from django.test import TestCase

from app.home.views import HomeView, JSView

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
