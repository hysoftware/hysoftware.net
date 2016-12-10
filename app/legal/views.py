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

    @cached_property
    def users_info(self):
        """Return hysoft staff's information."""
        from ..user.models import UserInfo
        return UserInfo.objects

    @cached_property
    def assets_info(self):
        """Retrn third party asset model."""
        from ..common.models import ThirdPartyAssets
        return ThirdPartyAssets.objects


class CSSView(TemplateView):
    """CSS view."""

    template_name = "legal.css"
    content_type = "text/css"


class JSView(TemplateView):
    """JS View."""

    template_name = "legal.js"
    content_type = "application/javascript"
