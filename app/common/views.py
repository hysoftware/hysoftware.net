#!/usr/bin/env python
# coding=utf-8

"""Common module views."""

from django.views.generic import TemplateView


class JSView(TemplateView):
    """Javascript view."""

    template_name = "common.js"
    content_type = "application/javascript"


class CSSView(TemplateView):
    """CSS view."""

    template_name = "common.css"
    content_type = "text/css"
