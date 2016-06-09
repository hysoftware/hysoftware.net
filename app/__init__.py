#!/usr/bin/env python
# coding=utf-8

"""The webapp."""

import os

from flask import Flask
from flask.ext.wtf.csrf import CsrfProtect, generate_csrf
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.admin.base import Admin, MenuLink

from .common import minify_html, HomeAdminView
from .contact import route as contact_bp
from .about import route as about_bp
from .home import route as home_bp
from .fonts import route as fonts_bp

from .user import route as user_bp, PersonAdmin
from .user.models import Person

cfgmap = {
    "production": "app.config.ProductionConfig",
    "devel": "app.config.DevelConfig"
}

app = Flask(__name__)
app.config.from_object(cfgmap[os.environ.get("mode", "devel")])
login_manager = LoginManager(app)
admin = Admin(app, index_view=HomeAdminView(url="/manage"))
MongoEngine(app)
CsrfProtect(app)
DebugToolbarExtension(app)

app.register_blueprint(about_bp, url_prefix="/about")
app.register_blueprint(contact_bp, url_prefix="/contact")
app.register_blueprint(home_bp)
if app.debug:
    app.register_blueprint(fonts_bp, url_prefix="/fonts")
app.register_blueprint(user_bp, url_prefix="/u")
admin.add_link(MenuLink(name="Back to HYSOFT", url="/#/"))
admin.add_view(PersonAdmin(Person))


@app.after_request
def html_minification(resp):
    """Minify HTML when response mimetype is text/html."""
    if resp.mimetype == "text/html":
        resp.data = minify_html(resp.data.decode("utf-8"))
    return resp


@login_manager.user_loader
def load_user(user_id):
    """Load user."""
    try:
        return Person.objects(pk=user_id).get()
    except Person.DoesNotExist:
        return None


@app.after_request
def csrf_prevent(resp):
    """Add CSRF Preventation for angularJS."""
    resp.set_cookie("X-CSRFToken", generate_csrf())
    return resp


@app.after_request
def prevent_clickjack(resp):
    """Prevent ClickJack exploit."""
    resp.headers["X-Frame-Options"] = "DENY"
    return resp


__all__ = ("app")
