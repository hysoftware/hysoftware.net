#!/usr/bin/env python
# coding=utf-8

"""Legal notification page controller."""

from flask import render_template
from flask.ext.classy import FlaskView


class LegalView(FlaskView):
    """Legal Notation."""

    trailing_slash = False

    def index(self):
        """Render Legal Notation."""
        regulations = [
            (
                "scta",
                "Notation based on the Specified Commercial Transaction Act",
                "scta.html", True
            )
        ]
        return render_template("legal.html", regulations=regulations)
