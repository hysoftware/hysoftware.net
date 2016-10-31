#!/usr/bin/env python
# coding=utf-8

"""Home views."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home Template View."""

    template_name = "home.html"

# Create your views here.
