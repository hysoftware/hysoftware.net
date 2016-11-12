#!/usr/bin/env python
# coding=utf-8

"""Administration panel for legal notation."""

from django.contrib import admin
from .models import NotationTable, Act, RecognizedCountry


class NotationTableAdmin(admin.TabularInline):
    """Notation table admin control."""

    model = NotationTable


@admin.register(Act)
class ActInline(admin.ModelAdmin):
    """Act inline admin view."""

    model = Act
    inlines = (NotationTableAdmin, )
    list_display = ("name", "description", "country")
    search_fields = ("name", "description", "country")


@admin.register(RecognizedCountry)
class LegalAdmin(admin.ModelAdmin):
    """Legal admin panel."""

    pass
