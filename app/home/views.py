#!/usr/bin/env python
# coding=utf-8

"""Home views."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home Template View."""

    template_name = "home.html"


class JSView(TemplateView):
    """Home front-end script view."""

    template_name = "home.js"
    content_type = "application/javascript"

# Create your views here.
