#!/usr/bin/env python
# coding=utf-8

"""Admin panel for user related models."""
from django.contrib import admin
from .models import UserInfo, TaskLog


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    """User info admin panel."""

    list_display = ("user",)


@admin.register(TaskLog)
class TaskLog(admin.ModelAdmin):
    """Task log form celery."""

    list_display = ("log_date", "user", "title", "message")
    search_fields = (
        "user__email", "user__first_name", "user__last_name", "user__username",
        "title", "message", "log_date"
    )
    readonly_fields = ("title", "message", "user", "log_date")
