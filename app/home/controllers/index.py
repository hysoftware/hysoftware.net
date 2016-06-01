#!/usr/bin/env python
# coding=utf-8

"""Home controller."""

from random import choice

from flask import render_template, session
from flask.ext.classy import FlaskView


class IndexView(FlaskView):
    """Home controller."""

    route_base = "/"
    website_taglines = [
        "Agile Software Development Professional",
        "Software Engineer Who Works Globally",
        "Great Software Engineer for Startups",
        "Code, Design, and contribute with a strong adherence of products"
    ]

    def index(self):
        """Main page resource."""
        session["tagline"] = choice(self.website_taglines)
        return render_template("index.html", tagline=session["tagline"])
