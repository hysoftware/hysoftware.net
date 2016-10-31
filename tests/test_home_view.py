#!/usr/bin/env python
# coding=utf-8

"""Test home view."""

from django.test import TestCase

from app.home.views import HomeView

from .view_base import TemplateViewTestBase


class HomeViewRenderingTest(TemplateViewTestBase, TestCase):
    """Home View Rendering Test."""

    template_name = "home.html"
    endpoint = "home:index"
    page_url = "/"
    view_cls = HomeView
