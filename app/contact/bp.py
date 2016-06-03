#!/usr/bin/env python
# coding=utf-8

"""Blue Print for contact."""

from flask import Blueprint
from .controllers import ContactView

route = Blueprint(
    "contact", __name__,
    static_folder="assets", template_folder="templates"
)

ContactView.register(route, route_base="/")
