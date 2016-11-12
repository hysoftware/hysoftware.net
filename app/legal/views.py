#!/usr/bin/env python
# coding=utf-8

"""Controllers for legal notation."""

from django.views.generic import TemplateView


class LegalView(TemplateView):
    """Legal view."""

    template_name = "legal.html"


class CSSView(TemplateView):
    """Template view."""

    template_name = "legal.css"
    content_type = "text/css"
