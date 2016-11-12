#!/usr/bin/env python
# coding=utf-8

"""Controllers for legal notation."""

from django.views.generic import TemplateView


class LegalView(TemplateView):
    """Legal view."""

    template_name = "legal.html"
