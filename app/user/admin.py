#!/usr/bin/env python
# coding=utf-8

"""Admin panel for user related models."""

from celery import current_app as ctask
from django.contrib import admin
from .models import UserInfo, TaskLog, GithubProfile


class GithubProfileAdminView(admin.TabularInline):
    """
    Github Profile Admin panel.

    But, this is readonly.
    """

    model = GithubProfile
    readonly_fields = ("avatar_url", "html_url", "bio")


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    """User info admin panel."""

    list_display = ("user",)
    readonly_fields = ("id", )
    inlines = (GithubProfileAdminView, )

    def save_model(self, req, obj, form, change):
        """Save the model and execute user.github.fetch task."""
        super(UserInfoAdmin, self).save_model(req, obj, form, change)
        ctask.send_task("user.github.fetch", (obj.id, ))


@admin.register(TaskLog)
class TaskLog(admin.ModelAdmin):
    """Task log form celery."""

    list_display = ("log_date", "user", "title", "message")
    search_fields = (
        "user__email", "user__first_name", "user__last_name", "user__username",
        "title", "message", "log_date"
    )
    readonly_fields = ("title", "message", "user", "log_date")
