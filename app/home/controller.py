#!/usr/bin/env python
# coding=utf-8

from flask.ext.classy import FlaskView
from flask import render_template


class IndexView(FlaskView):
    route_base = "/"

    def index(self):
        return render_template("index.html")
