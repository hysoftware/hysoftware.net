#!/usr/bin/env python
# coding=utf-8

"""Jinja2 env."""

from jinja2 import Environment


def jinja_options(**env):
    """Set jinja env."""
    environ = Environment(**env)
    return environ
