#!/usr/bin/env python
# coding=utf-8

"""Controllers for legal notation."""

from django.views.generic import TemplateView
from django.utils.functional import cached_property


class LegalView(TemplateView):
    """Legal view."""

    template_name = "legal.html"

    @cached_property
    def country(self):
        """Return countries where the required notation is recognized."""
        from .models import RecognizedCountry
        return RecognizedCountry.objects


class CSSView(TemplateView):
    """Template view."""

    template_name = "legal.css"
    content_type = "text/css"
