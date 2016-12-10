#!/usr/bin/env python
# coding=utf-8

"""Home views."""

from django.utils.functional import cached_property
from django.utils.translation import get_language_from_request
from django.views.generic import TemplateView


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


class CSSView(TemplateView):
    """Home stylesheet view."""

    template_name = "home.css"
    content_type = "text/css"
