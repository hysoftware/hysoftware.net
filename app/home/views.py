#!/usr/bin/env python
# coding=utf-8

"""Home views."""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.utils.translation import get_language_from_request
from django.views.generic import TemplateView, View


class HomeView(TemplateView):
    """Home Template View."""

    template_name = "home.html"

    @cached_property
    def users_info(self):
        """Get users info."""
        from ..user.models import UserInfo
        return UserInfo.objects

    @cached_property
    def pitch(self):
        """Get pitch."""
        from .models import Pitch
        pitch = Pitch.objects.choice()
        return getattr(pitch, ("text_{}").format(
            get_language_from_request(self.request).replace("-", "_")
        ), None) or pitch.text


class JSView(TemplateView):
    """Home front-end script view."""

    template_name = "home.js"
    content_type = "application/javascript"


class CSSView(TemplateView):
    """Home stylesheet view."""

    template_name = "home.css"
    content_type = "text/css"


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
