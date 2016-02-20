#!/usr/bin/env python
# coding=utf-8

import os
import htmlmin

from flask import Flask
from flask.ext.wtf.csrf import CsrfProtect, generate_csrf
from flask.ext.debugtoolbar import DebugToolbarExtension

from .home import home

cfgmap = {
    "production": "app.config.ProductionConfig",
    "devel": "app.config.DevelConfig"
}

app = Flask(__name__)
app.config.from_object(
    cfgmap[os.environ.get("mode", "devel")]
)
DebugToolbarExtension(app)
CsrfProtect(app)

app.register_blueprint(home)


@app.after_request
def html_minification(resp):
    '''
    Minify HTML when response mimetype is text/html
    '''
    if resp.mimetype == "text/html":
        resp.data = htmlmin.minify(
            resp.data.decode("utf-8"),
            remove_comments=True,
            remove_empty_space=True,
            remove_optional_attribute_quotes=False
        )
    return resp


@app.after_request
def csrf_prevent(resp):
    '''
    Add CSRF Preventation for angularJS
    '''

    resp.set_cookie("X-CSRFToken", generate_csrf())
    return resp


__all__ = ["app"]
