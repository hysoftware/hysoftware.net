#!/usr/bin/env python
# coding=utf-8

"""Common administration panel."""

from django.contrib import admin
from .models import ThirdPartyAssets


@admin.register(ThirdPartyAssets)
class ThirdPartyAssetsAdmin(admin.ModelAdmin):
    """Third party assets admin."""

    list_display = ("filename", "image", "license", "license_url")
    search_fields = list_display
