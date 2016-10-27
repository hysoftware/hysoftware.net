#!/usr/bin/env python
# coding=utf-8

"""Jinja2 env."""

from jinja2 import Environment

from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.finders import find


def __static_exists__(path):
    """Check whether the specified path exists on static file or not."""
    return bool(find(path, all=True))


def jinja_options(**env):
    """Set jinja env."""
    environ = Environment(**env)
    environ.globals.update({
        "static": staticfiles_storage.url,
        "static_exists": __static_exists__
    })
    return environ
