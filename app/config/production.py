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
        "host": os.environ.get("db_url", None),
        "username": os.environ.get("db_user", None),
        "password": os.environ.get("db_password", None)
    }
    RECAPTCHA_USE_SSL = True
    RECAPTCHA_PUBLIC_KEY = os.environ["recaptcha_pubkey"]
    RECAPTCHA_PRIVATE_KEY = os.environ["recaptcha_prikey"]
    MAIL_SERVER = os.environ["MAIL_SERVER"]
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "True").lower() == "true"
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", "False").lower() == "true"
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587)) or 587
    MAIL_USERNAME = os.environ["MAIL_USERNAME"]
    MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
