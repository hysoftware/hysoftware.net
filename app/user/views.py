#!/usr/bin/env python
# coding=utf-8

"""About member view."""

import json

from django.shortcuts import get_object_or_404
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

    @cached_property
    def user_info(self):
        """Return the user information."""
        from .models import UserInfo
        return get_object_or_404(UserInfo, id=self.kwargs["info_id"])


class ContactView(TemplateView):
    """Contact view."""

    template_name = "contact.html"

    @cached_property
    def user_info(self):
        """Return the user information."""
        from .models import UserInfo
        return get_object_or_404(UserInfo, id=self.kwargs["info_id"])

    @cached_property
    def users_info(self):
        """Return UserInfo.objects."""
        from .models import UserInfo
        return UserInfo.objects

    @cached_property
    def form(self):
        """Return contact form."""
        from .forms import ContactForm
        return ContactForm(json.loads(
            self.request.body.decode("utf-8")
        )) if self.request.body else ContactForm()


class CSSView(TemplateView):
    """CSS view."""

    template_name = "user.css"
    content_type = "text/css"


class JSView(TemplateView):
    """JSView."""

    template_name = "user.js"
    content_type = "application/javascript"
