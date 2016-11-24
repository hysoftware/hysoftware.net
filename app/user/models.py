#!/usr/bin/env python
# coding=utf-8

"""Database models for user module."""

import uuid
from collections import OrderedDict

from django.conf import settings
from django.utils.translation import ugettext_lazy as _lz

from django.db import models as db


class UserInfo(db.Model):
    """User info."""

    class Meta(object):
        """Metadata."""

        verbose_name = _lz("User Info")
        verbose_name_plural = _lz("User Info")

    availability_choices = OrderedDict((
        ("FL", _lz("Available for Full-Time and Part-Time position")),
        ("PT", _lz("Available for Part-Time position only")),
        ("NA", _lz("Busy"))
    ))
    id = db.UUIDField(primary_key=True, default=uuid.uuid4)
    user = db.OneToOneField(settings.AUTH_USER_MODEL)
    title = db.CharField(max_length=40, db_index=True)
    github = db.CharField(max_length=39, unique=True)
    linkedin = db.URLField(db_index=True, blank=True, null=True)
    availability = db.CharField(
        max_length=2, db_index=True, choices=availability_choices.items()
    )
    angel_co = db.CharField(
        max_length=80, db_index=True, blank=True, null=True
    )
    hacker_rank = db.CharField(
        max_length=17, db_index=True, blank=True, null=True
    )


class GithubProfile(db.Model):
    """Github profile."""

    user_info = db.OneToOneField(UserInfo, related_name="github_profile")
    avatar_url = db.URLField()
    html_url = db.URLField()
    bio = db.CharField(max_length=160, blank=True, null=True)


class TaskLog(db.Model):
    """Celery task logs."""

    user = db.ForeignKey(settings.AUTH_USER_MODEL)
    log_date = db.DateTimeField(auto_now_add=True)
    title = db.CharField(max_length=250)
    message = db.TextField()
