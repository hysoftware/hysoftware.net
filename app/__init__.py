#!/usr/bin/env python
# coding=utf-8

import os

from flask import Flask
from flask.ext.wtf import CsrfProtect
from flask.ext.debugtoolbar import DebugToolbarExtension

from .home import home

cfgmap = {
    "production": "app..config.ProductionConfig",
    "devel": "app.config.DevelConfig"
}

app = Flask(__name__)
app.config.from_object(
    cfgmap.get(os.environ.get("mode", "devel"), "app.config.DevelConfig")
)
DebugToolbarExtension(app)
CsrfProtect(app)

app.register_blueprint(home)


__all__ = ["app"]
