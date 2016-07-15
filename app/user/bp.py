#!/usr/bin/env python
# coding=utf-8

"""User blueprint."""

from flask import Blueprint
from .controllers import LoginView, QRCode

route = Blueprint(
    "user", __name__, static_folder="assets", template_folder="templates"
)
LoginView.register(route)
QRCode.register(route)
