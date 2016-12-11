#!/usr/bin/env python
# coding=utf-8

"""Config for public."""

import re
import os

from .devel import DevelConfig


class PublicConfig(DevelConfig):
    """Config for production."""

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
    RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]
    MAILGUN_KEY = os.environ["MAILGUN_KEY"]
    MAILGUN_URL = os.environ["MAILGUN_URL"]
    ALLOWED_HOSTS = re.split(",\\s.", os.environ["ALLOWED_HOSTS"])
    CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]
    CELERY_RESULT_BACKEND = None
    CELERY_BROKER_TRANSPORT_OPTIONS = {
        "region": os.environ["SQS_REGION"],
        "queue_name_prefix": os.environ["SQS_PREFIX"]
    }
