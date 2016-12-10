#!/usr/bin/env python
# coding=utf-8

"""Config for public."""

import os

from .devel import DevelConfig


class PublicConfig(DevelConfig):
    """Config for production."""

    SECRET_KEY = os.environ["SECRET"]
    RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]
    MAILGUN_KEY = os.environ["MAILGUN_KEY"]
    MAILGUN_URL = os.environ["MAILGUN_URL"]
