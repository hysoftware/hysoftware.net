#!/usr/bin/env python
# coding=utf-8

"""Login controllers."""

from flask import render_template
from flask.ext.classy import FlaskView
from ..forms import LoginForm


class LoginView(FlaskView):
    """Login Controller."""

    trailing_slash = False

    def index(self):
        """index."""
        return render_template("login.html", form=LoginForm())
