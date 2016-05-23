#!/usr/bin/env python
# coding=utf-8

from random import choice

from flask import render_template
from flask.ext.classy import FlaskView

from ...common import minify_html


class IndexView(FlaskView):
    route_base = "/"
    website_taglines = [
        "Agile Software Development Professional",
        "Software Engineer Who Works Globally",
        "Great Software Engineer for Startups",
        "Code, Design, and contribute with a strong adherence of products"
    ]

    def index(self):
        '''
        Main page resource
        '''
        return render_template(
            "index.html", tagline=choice(self.website_taglines),
            minify=minify_html
        )
