#!/usr/bin/env python
# coding=utf-8

"""About member view."""

from django.views.generic import TemplateView


class AboutView(TemplateView):
    """About page."""

    template_name = "about.html"
