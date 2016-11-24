#!/usr/bin/env python
# coding=utf-8

"""About member view."""

from django.views.generic import TemplateView
from django.utils.functional import cached_property


class AboutView(TemplateView):
    """About page."""

    template_name = "about.html"

    @cached_property
    def users_info(self):
        """Return users information."""
        from .models import UserInfo
        return UserInfo.objects


class MemberDialog(TemplateView):
    """Staff Dialog."""

    template_name = "member_dialog.html"


class CSSView(TemplateView):
    """CSS view."""

    template_name = "user.css"
    content_type = "text/css"
