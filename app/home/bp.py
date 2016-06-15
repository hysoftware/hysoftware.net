#!/usr/bin/env python
# coding=utf-8

"""Blueprint for homepage."""

from flask import Blueprint
from .controllers import IndexView, HomeView


route = Blueprint(
    "home", __name__,
    static_folder="assets",
    template_folder="templates"
)
IndexView.register(route)
HomeView.register(route)
