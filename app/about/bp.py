#!/usr/bin/env python
# coding=utf-8

"""Blueprint for about pages."""

from flask import Blueprint
from .controllers import LegalView

route = Blueprint(
    "about", __name__,
    static_folder="assets",
    template_folder="templates"
)

LegalView.register(route)
