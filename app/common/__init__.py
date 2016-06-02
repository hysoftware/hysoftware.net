#!/usr/bin/env python
# coding=utf-8

"""Functionalities that is used commonly."""

from .htmlminify import minify_html
from .admin import AdminModelBase
from .forms import DelayedSelectField

__all__ = ("minify_html", "AdminModelBase", "DelayedSelectField")
