#!/usr/bin/env python
# coding=utf-8

"""Login controllers."""

import json
from flask import render_template, jsonify, make_response, abort
from flask.ext.classy import FlaskView
from flask.ext.login import (
    login_user, logout_user, current_user, login_required
)
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

    @login_required
    def status(self):
        """Return your information."""
        you = json.loads(current_user.to_json())
        for exclude in ["code", "id", "is_authenticated", "is_active"]:
            you.pop(exclude, None)
        return jsonify(you)

    def delete(self):
        """Logout."""
        logout_user()
        return "", 200
