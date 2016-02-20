#!/usr/bin/env python
# coding=utf-8

from random import choice

from flask import render_template
from flask.ext.classy import FlaskView


class IndexView(FlaskView):
    route_base = "/"
    website_taglines = [
        "Agile Software Development Professional",
        "Software Engineer Who Works Globally",
        "Great Software Engineer for Startups",
        "Code, Design, and Friendly with passion"
    ]

    def index(self):
        return render_template(
            "index.html", tagline=choice(self.website_taglines)
        )
