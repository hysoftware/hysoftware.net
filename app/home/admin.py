#!/usr/bin/env python
# coding=utf-8

"""Admin panel."""

import django.contrib.admin as admin

from .models import Pitch


@admin.register(Pitch)
class PitchAdmin(admin.ModelAdmin):
    """Pitch Admin Panel."""

    list_filter = ("text", )
