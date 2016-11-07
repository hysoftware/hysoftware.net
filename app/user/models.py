#!/usr/bin/env python
# coding=utf-8

"""Database models for user module."""

from django.conf import settings
from django.utils.translation import ugettext_lazy as _lz

from django.db import models as db


class UserInfo(db.Model):
    """User info."""

    class Meta(object):
        """Metadata."""

        verbose_name = _lz("User Info")
        verbose_name_plural = _lz("User Info")

    user = db.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True, db_index=True
    )
    github = db.CharField(max_length=39, unique=True, db_index=True)
