#!/usr/bin/env python
# coding=utf-8

"""Blueprint for about pages."""

from flask import Blueprint
from .controllers import LegalView, TeamView

route = Blueprint(
    "about", __name__,
    static_folder="assets",
    template_folder="templates"
)

LegalView.register(route)
TeamView.register(route, route_base="/")
