#!/usr/bin/env python
# coding=utf-8

"""Admin base."""

from flask import abort
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.mongoengine import ModelView
from flask_wtf import Form
from flask_login import current_user


class AdminModelBase(ModelView):
    """Admin model view."""

    form_base_class = Form

    def is_accessible(self):
        """Check whether the user can access admin panel or not."""
        return current_user.is_authenticated and \
            "admin" in current_user.role

    def inaccessible_callback(self, name, **kwargs):
        """Redirect to home if the user is not accessible."""
        abort(404)


class HomeAdminView(AdminIndexView):
    """Home admin view that aborts 404 if the user is not authorized."""

    @expose("/")
    def index(self):
        """Index request."""
        if not (current_user.is_authenticated and
                "admin" in current_user.role):
            abort(404)
        return super(HomeAdminView, self).index()
