#!/usr/bin/env python
# coding=utf-8

"""Common module views."""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.views.generic import TemplateView, View


class JSView(TemplateView):
    """Javascript view."""

    template_name = "common.js"
    content_type = "application/javascript"


class CSSView(TemplateView):
    """CSS view."""

    template_name = "common.css"
    content_type = "text/css"


class ImageView(View):
    """Home Title Image View."""

    @cached_property
    def image(self):
        """Load Image from the db."""
        from ..common.models import ThirdPartyAssets
        return get_object_or_404(
            ThirdPartyAssets, filename=self.kwargs["filename"]
        )

    def get(self, request, filename):
        """Show title image."""
        obj = self.image
        return HttpResponse(obj.image.read(), content_type="image/jpeg")
