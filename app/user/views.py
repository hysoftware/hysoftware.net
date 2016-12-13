#!/usr/bin/env python
# coding=utf-8

"""About member view."""

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.utils.functional import cached_property
from django.utils.translation import (
    ungettext as _n, ugettext_lazy as _lz
)


class AboutView(TemplateView):
    """About page."""

    template_name = "about.html"

    @cached_property
    def description(self):
        """Return description of this page."""
        return _n("About me", "About us", self.users_info.count())

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
    description = _lz("Contact Form")

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
        )) if self.request.body else ContactForm(
            info_id=self.kwargs["info_id"]
        ) if self.kwargs["info_id"] else ContactForm()

    def post(self, req, **kwargs):
        """Store the message and email to the customer and me."""
        form = self.form
        if not form.is_valid():
            return JsonResponse(form.errors, status=417)
        form.save()
        return HttpResponse("", status=200)


class CSSView(TemplateView):
    """CSS view."""

    template_name = "user.css"
    content_type = "text/css"


class JSView(TemplateView):
    """JSView."""

    template_name = "user.js"
    content_type = "application/javascript"
