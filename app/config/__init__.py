#!/usr/bin/env python
# coding=utf-8

'''
App configurations
'''

import os

mode = os.environ.get("mode", "devel")


if mode == "devel":
    from .devel import DevelConfig

if mode == "production":
    from .production import ProductionConfig


__all__ = ["ProductionConfig", "DevelConfig"]
