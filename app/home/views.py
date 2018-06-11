#!/usr/bin/env python
# coding=utf-8

"""Home views."""

from django.conf import settings
from django.views.generic import TemplateView
from hysoftware_data.home import pitch as subtitles
from hysoftware_data.users import Users


class HomeView(TemplateView):
    """Home Template View."""

    template_name = "home.html"
    users = Users(settings.NAME)
    pitches = subtitles.Pitch()

    @property
    def users_info(self):
        """Get users info."""
        return self.users

    @property
    def pitch(self):
        """Get pitch."""
        return self.pitches.choice


class SSLValidationView(TemplateView):
    """SSL validation view."""

    template_name = "A19129EBDFBB9D747449765BAEB1C234.txt"
    content_type = "text/plain"
