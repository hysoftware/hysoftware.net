#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint
from .controller import OpenSansView


route = Blueprint(
    "fonts", __name__,
    static_folder="assets",
    template_folder="templates"
)

OpenSansView.register(route)
