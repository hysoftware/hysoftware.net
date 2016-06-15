#!/usr/bin/env python
# coding=utf-8

"""About team controller."""

from flask import render_template
from flask.ext.classy import FlaskView

from ...user.models import Person


class TeamView(FlaskView):
    """Team view."""

    trailing_slash = False

    def index(self):
        """Index request."""
        members = Person.objects(role__in=["member"])
        return render_template("team.html", model=members)
