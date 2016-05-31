#!/usr/bin/env python
# coding=utf-8

"""Functionalities that is used commonly."""

from .htmlminify import minify_html
from .admin import AdminModelBase

__all__ = ("minify_html", "AdminModelBase")
