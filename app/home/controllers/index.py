#!/usr/bin/env python
# coding=utf-8

"""Home controller."""

from random import choice

from flask import render_template, session
from flask.ext.classy import FlaskView, route
from flask.ext.login import current_user


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
        return render_template(
            "index.html", tagline=session["tagline"],
            current_user=current_user
        )

    @route("/ED512523231BF2C276F941231D7AC53D.txt")
    def ssl_validation(self):
        """Send validation text to validate SSL."""
        return render_template("ED512523231BF2C276F941231D7AC53D.txt")
