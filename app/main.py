#!/usr/bin/env python
# coding=utf-8

import os

from flask import Flask

from .config import ProductionConfig, DevelConfig

cfgmap = {
    "production": ProductionConfig,
    "devel": DevelConfig
}

app = Flask(__name__)
app.config.from_object(
    cfgmap.get(os.environ.get("mode", "devel"), DevelConfig)
)
