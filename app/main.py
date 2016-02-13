#!/usr/bin/env python
# coding=utf-8

import os

from flask import Flask
from flask.ext.wtf import CsrfProtect

from .config import ProductionConfig, DevelConfig
from .home import home

cfgmap = {
    "production": ProductionConfig,
    "devel": DevelConfig
}

app = Flask(__name__)
app.config.from_object(
    cfgmap.get(os.environ.get("mode", "devel"), DevelConfig)
)
CsrfProtect(app)

app.register_blueprint(home)

if __name__ == '__main__':
    app.run(
        host=os.environ.get("host", None),
        port=os.environ.get("port", None),
        threaded=True
    )
