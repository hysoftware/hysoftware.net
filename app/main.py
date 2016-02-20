#!/usr/bin/env python
# coding=utf-8

import os

from flask import Flask
from flask.ext.wtf import CsrfProtect

from .home import home

cfgmap = {
    "production": "app..config.production.ProductionConfig",
    "devel": "app.config.devel.DevelConfig"
}

app = Flask(__name__)
app.config.from_object(cfgmap.get[os.environ.get("mode", "devel")])
CsrfProtect(app)

app.register_blueprint(home)


__all__ = [
    "app"
]
