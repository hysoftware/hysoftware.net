#!/usr/bin/env python
# coding=utf-8

"""Configuration for testing."""


from .devel import DevelConfig


class TestConfig(DevelConfig):
    """Configuration for testing."""

    DEBUG = False
    TEMPLATE_DEBUG = False

    PASSWORD_HASHERS = (
        "django.contrib.auth.hashers.MD5PasswordHasher",
    )

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]
