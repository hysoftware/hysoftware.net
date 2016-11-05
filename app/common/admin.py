#!/usr/bin/env python
# coding=utf-8

"""Common administration panel."""

from django.contrib import admin
from .models import ThirdPartyAssets


@admin.register(ThirdPartyAssets)
class ThirdPartyAssetsAdmin(admin.ModelAdmin):
    """Third party assets admin."""

    pass
