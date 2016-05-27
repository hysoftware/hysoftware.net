#!/usr/bin/env python
# coding=utf-8

"""The webapp."""

import os

from flask import Flask
from flask.ext.wtf.csrf import CsrfProtect
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

from .common import minify_html
from .about import route as about_bp
from .home import route as home_bp
from .fonts import route as fonts_bp

from .user import route as user_bp
from .user.models import Person

cfgmap = {
    "production": "app.config.ProductionConfig",
    "devel": "app.config.DevelConfig"
}

app = Flask(__name__)
app.config.from_object(
    cfgmap[os.environ.get("mode", "devel")]
)
login_manager = LoginManager(app)
MongoEngine(app)
CsrfProtect(app)
DebugToolbarExtension(app)

app.register_blueprint(about_bp, url_prefix="/about")
app.register_blueprint(home_bp)
if app.debug:
    app.register_blueprint(fonts_bp, url_prefix="/fonts")
app.register_blueprint(user_bp, url_prefix="/u")


@app.after_request
def html_minification(resp):
    """Minify HTML when response mimetype is text/html."""
    if resp.mimetype == "text/html":
        resp.data = minify_html(resp.data.decode("utf-8"))
    return resp


@login_manager.user_loader
def load_user(user_id):
    """Load user."""
    return Person.objects(id=user_id).get()


# @app.after_request
# def csrf_prevent(resp):
#     """Add CSRF Preventation for angularJS."""
#     resp.set_cookie("X-CSRFToken", generate_csrf())
#     return resp


__all__ = ("app",)
