#!/usr/bin/env python
# coding=utf-8

"""Config on production mode."""

import os


class ProductionConfig(object):
    """Production config."""

    BUGTRACKER = os.environ.get(
        "issue", "https://github.com/hysoftware/hysoftware.net"
    )
    SECRET_KEY = os.environ["secret"]
    SESSION_COOKIE_SECURE = os.environ.get("cookie_secure", False)
    PREFERRED_URL_SCHEME = os.environ.get("url_scheme", "http")
    WTF_CSRF_METHODS = ["POST", "PUT", "PATCH", "DELETE"]
    MONGODB_SETTINGS = {
        "db": os.environ.get("db_url", "").split("/")[-1] or None,
        "host": os.environ.get("db_url", None),
        "username": os.environ.get("db_user", None),
        "password": os.environ.get("db_password", None)
    }
    RECAPTCHA_USE_SSL = True
    RECAPTCHA_PUBLIC_KEY = os.environ["recaptcha_pubkey"]
    RECAPTCHA_PRIVATE_KEY = os.environ["recaptcha_prikey"]
    MAILGUN_API = os.environ["MAILGUN_API"]
    MAILGUN_URL = os.environ["MAILGUN_URL"]
