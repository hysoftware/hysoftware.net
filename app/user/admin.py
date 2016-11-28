#!/usr/bin/env python
# coding=utf-8

"""Admin panel for user related models."""

from celery import current_app as ctask
from django.contrib import admin
from .models import (
    UserInfo, TaskLog, GithubProfile, CodingLanguage, Framework,
    Hobby
)


class GithubProfileAdminView(admin.TabularInline):
    """
    Github Profile Admin panel.

    But, this is readonly.
    """

    model = GithubProfile
    readonly_fields = ("avatar_url", "html_url", "bio")


@admin.register(CodingLanguage)
class CodingLanguageAdmin(admin.ModelAdmin):
    """Coding langauge admin panel."""

    list_display = ("name", )
    search_fields = (
        "name", "users_info__user__email", "users_info__user__first_name",
        "users_info__user__last_name"
    )


@admin.register(Framework)
class FrameowrkAdmin(admin.ModelAdmin):
    """Framework admin."""

    list_display = (
        "name", "icon_cls", "icon_body", "url", "description"
    )
    search_fields = list_display + (
        "languages__name",
        "users_info__user__email", "users_info__user__first_name",
        "users_info__user__last_name"
    )


class HobbyPanel(admin.TabularInline):
    """Member's hobby."""

    model = Hobby


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    """User info admin panel."""

    list_display = ("user",)
    readonly_fields = ("id", )
    inlines = (GithubProfileAdminView, HobbyPanel)

    def save_model(self, req, obj, form, change):
        """Save the model and execute user.github.fetch task."""
        super(UserInfoAdmin, self).save_model(req, obj, form, change)
        ctask.send_task("user.github.fetch", (str(obj.id), ))


@admin.register(TaskLog)
class TaskLog(admin.ModelAdmin):
    """Task log form celery."""

    list_display = ("log_date", "user", "title", "message")
    search_fields = (
        "user__email", "user__first_name", "user__last_name", "user__username",
        "title", "message", "log_date"
    )
    readonly_fields = ("title", "message", "user", "log_date")
