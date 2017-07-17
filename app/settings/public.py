#!/usr/bin/env python
# coding=utf-8

"""Config for public."""

# import json
import re
import os

from .devel import DevelConfig


class PublicConfig(DevelConfig):
    """Config for production."""

    DEBUG = True
    THIRD_PARTY_APPS = DevelConfig.THIRD_PARTY_APPS + ["storages"]
    INSTALLED_APPS = \
        DevelConfig.BUILTIN_APPS + THIRD_PARTY_APPS + DevelConfig.MODULES
    SECRET_KEY = os.environ["SECRET"]
    DATABASES = {
        "default": {
            "ENGINE": os.environ["DB_ENGINE"],
            "NAME": os.environ["DB_NAME"],
            "USER": os.environ["DB_USER"],
            "PASSWORD": os.environ["DB_PW"],
            "HOST": os.environ["DB_HOST"],
            "PORT": os.environ["DB_PORT"]
        }
    }

    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    # AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    # AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]

    RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]
    MAILGUN_KEY = os.environ["MAILGUN_KEY"]
    MAILGUN_URL = os.environ["MAILGUN_URL"]
    ALLOWED_HOSTS = re.split(",\\s*", os.environ["ALLOWED_HOSTS"])
    CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
    # CELERY_BROKER_TRANSPORT_OPTIONS = json.loads(
    #     os.environ.get("CELERY_BROKER_TRANSPORT_OPTIONS") or "null"
    # )
    SESSION_COOKIE_SECURE = \
        os.environ.get("COOKIE_SECURE", "false").lower() == "true"
    CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE
    SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", "0"))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = \
        os.environ.get(
            "SECURE_HSTS_INCLUDE_SUBDOMAINS", "false"
        ).lower() == "true"
