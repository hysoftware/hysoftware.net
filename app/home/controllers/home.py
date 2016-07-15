#!/usr/bin/env python
# coding=utf-8

"""Home view."""

from random import choice

from flask import render_template, session
from flask_classy import FlaskView

from .index import IndexView
from ...contact.forms import ContactForm


class HomeView(FlaskView):
    """Home view."""

    trailing_slash = False

    def index(self):
        """Index reosurce."""
        if "tagline" not in session:
            session["tagline"] = choice(IndexView.website_taglines)
        return render_template(
            "home.html", tagline=session["tagline"],
            contact_form=ContactForm()
        )
