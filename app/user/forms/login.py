#!/usr/bin/env python
# coding=utf-8

"""Login form."""

from flask.ext.wtf import Form
import wtforms.fields as fld
import wtforms.validators as vld


class LoginForm(Form):
    """Login form."""

    email = fld.StringField(validators=[vld.DataRequired(), vld.Email()])
    password = fld.PasswordField(validators=[vld.DataRequired()])
