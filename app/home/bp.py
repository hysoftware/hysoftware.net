#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint
from .controller import IndexView


route = Blueprint(
    "home", __name__,
    static_folder="static",
    template_folder="templates"
)
IndexView.register(route)
