#!/usr/bin/env python
# coding=utf-8

"""Common administration panel."""

from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import ThirdPartyAssets


@admin.register(ThirdPartyAssets)
class ThirdPartyAssetsAdmin(admin.ModelAdmin):
    """Third party assets admin."""

    class Meta(object):
        """Metadata."""

        verbose_name = _("Third Party Asset")
        verbose_name_plural = _("Third Party Assets")
