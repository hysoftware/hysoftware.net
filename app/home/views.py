#!/usr/bin/env python
# coding=utf-8

"""Home views."""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.views.generic import TemplateView, View


class HomeView(TemplateView):
    """Home Template View."""

    template_name = "home.html"


class JSView(TemplateView):
    """Home front-end script view."""

    template_name = "home.js"
    content_type = "application/javascript"


class HomeTitleImageView(View):
    """Home Title Image View."""

    @cached_property
    def image(self):
        """Load Image from the db."""
        from ..common.models import ThirdPartyAssets
        return get_object_or_404(ThirdPartyAssets, filename="home")

    def get(self, request):
        """Show title image."""
        obj = self.image
        return HttpResponse(obj.image.read(), content_type="image/jpeg")

# Create your views here.
