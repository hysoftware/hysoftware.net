#!/usr/bin/env python
# coding=utf-8

import os


class ProductionConfig(object):
    '''
    Production config
    '''
    SECRET_KEY = os.environ["secret"]
    SESSION_COOKIE_SECURE = os.environ.get("cookie_secure", False)
    PREFERRED_URL_SCHEME = os.environ.get("url_scheme", "http")
    MONGODB_SETTINGS = {
        "host": os.environ.get("db_url", None),
        "username": os.environ.get("db_user", None),
        "password": os.environ.get("db_password", None)
    }
