#!/usr/bin/env python
# coding=utf-8

"""Admin base."""

from flask import redirect
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.wtf import Form
from flask.ext.login import current_user


class AdminModelBase(ModelView):
    """Admin model view."""

    form_base_class = Form

    def is_accessible(self):
        """Check whether the user can access admin panel or not."""
        return current_user.is_authenticated and \
            "admin" in current_user.role

    def inaccessible_callback(self, name, **kwargs):
        """Redirect to home if the user is not accessible."""
        return redirect("/#/")