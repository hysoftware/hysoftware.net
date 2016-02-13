#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint

home = Blueprint(
    "home", __name__,
    static_folder="static",
    template_folder="templates"
)
