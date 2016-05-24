#!/usr/bin/env python
# coding=utf-8

"""App configurations."""

import os

mode = os.environ.get("mode", "devel")

if mode == "production":
    from .production import ProductionConfig
elif mode == "devel":
    from .devel import DevelConfig
else:
    EnvironmentError("Invalid mode is given")

__all__ = ("ProductionConfig", "DevelConfig")
