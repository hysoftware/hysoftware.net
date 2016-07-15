#!/usr/bin/env python
# coding=utf-8

"""Admin panel."""

from collections import OrderedDict

import wtforms.fields as fld
import wtforms.validators as vld
from wtf_otp import OTPSecretKeyField

from ..common import AdminModelBase
from .models import Person


class CurrentPasswordValidation(object):
    """Current password validation."""

    def __init__(self, fields):
        """Init obj."""
        self.fields = fields

    def __call__(self, form, field):
        """Validate."""
        model = Person.objects(email=form.email.data).first()
        if model is None:
            return

        if all([getattr(form, f).data for f in self.fields]):
            if not field.data:
                raise vld.ValidationError("This field is required.")
            if not model.verify(field.data):
                raise vld.ValidationError("The password wasn't matched.")


class PersonAdmin(AdminModelBase):
    """Person admin."""

    form_subdocuments = {
        "skills": {},
        "websites": {},
    }
    column_exclude_list = ("code", "sacode")
    form_excluded_columns = ("code", "sacode")
    form_extra_fields = OrderedDict([
        (
            "current_password", fld.PasswordField(
                validators=[
                    CurrentPasswordValidation([
                        "new_password", "confirm_password"
                    ])
                ]
            )
        ),
        ("new_password", fld.PasswordField()),
        (
            "confirm_password",
            fld.PasswordField(validators=[vld.EqualTo("new_password")])
        ), (
            "2FA_secret",
            OTPSecretKeyField(qrcode_url="/u/qrcode")
        )
    ])

    def on_model_change(self, form, model, is_created=False):
        """Apply new password."""
        if form.confirm_password.data:
            model.password = form.confirm_password.data
