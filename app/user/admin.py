#!/usr/bin/env python
# coding=utf-8

"""Admin panel for user related models."""
from django.contrib import admin
from .models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    """User info admin panel."""

    list_display = ("user",)
