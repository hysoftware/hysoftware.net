#!/usr/bin/env python
# coding=utf-8

"""Configuration for testing."""


from .devel import DevelConfig


class TestConfig(DevelConfig):
    """Configuration for testing."""

    DEBUG = False
    TEMPLATE_DEBUG = False

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]
    LANGUAGE_CODE = 'en-us'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
