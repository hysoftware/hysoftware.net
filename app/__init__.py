#!/usr/bin/env python
# coding=utf-8

"""HYSOFT webapp."""

from .celery_app import app as celery_app

__all__ = ("celery_app", )
