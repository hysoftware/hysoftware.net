#!/usr/bin/env python
# coding=utf-8

"""Login controllers."""

from flask import render_template, jsonify, make_response, abort
from flask.ext.classy import FlaskView
from flask.ext.login import login_user, logout_user
from ..forms import LoginForm
from ..models import Person


class LoginView(FlaskView):
    """Login Controller."""

    trailing_slash = False

    def index(self):
        """index."""
        return render_template("login.html", form=LoginForm())

    def post(self):
        """Login."""
        form = LoginForm()
        if not form.validate():
            return make_response(jsonify(form.errors), 417)
        person = Person.objects.get_or_404(email=form.email.data)
        if not person.verify(form.password.data):
            abort(404)
        login_user(person)
        return "", 200

    def delete(self):
        """Logout."""
        logout_user()
        return "", 200
