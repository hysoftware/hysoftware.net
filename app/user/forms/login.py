#!/usr/bin/env python
# coding=utf-8

"""Login form."""

from flask.ext.wtf import Form
import wtforms.fields as fld
import wtforms.fields.html5 as html5fld
import wtforms.validators as vld


class LoginForm(Form):
    """Login form."""

    email = html5fld.EmailField(
        "Email", validators=[vld.InputRequired(), vld.Email()],
        render_kw={
            "class": "form-control",
            "data-ng-model": "model.email",
            "required": True
        }
    )
    password = fld.PasswordField(
        "Password", validators=[vld.InputRequired()],
        render_kw={
            "class": "form-control",
            "data-ng-model": "model.password",
            "required": True
        }
    )
