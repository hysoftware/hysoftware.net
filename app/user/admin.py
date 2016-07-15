#!/usr/bin/env python
# coding=utf-8

"""Admin panel."""

from collections import OrderedDict

import wtforms.fields as fld
import wtforms.validators as vld
from wtf_otp import OTPSecretKeyField, OTPCheck

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


class ValidateTrue(object):
    """Validate the value with the specified validator."""

    def __init__(self, validator, exp, *args, **kwargs):
        """
        Initialize the class.

        Parameters:
            validator: The validator. The value is validated when the exp is
                Truthy.
            exp: Expression to check if vaidation is needed. Note that this
                can be callable with form and field params, and in this case,
                the exp is evaluated when __call__ is called.
            *args: Any arguments to be passed to the validator.
            **kwargs: Any keyword arguments to be passed to the validator.
        """
        self.validator = validator
        self.exp = exp
        self.args = args
        self.kwargs = kwargs

    def __call__(self, form, field):
        """
        Validate the field.

        Parameters:
            form: The form
            field: The field
        """
        exp = False
        try:
            exp = self.exp(form, field)
        except TypeError:
            exp = self.exp

        if exp:
            validation = self.validator(*self.args, **self.kwargs)
            return validation(form, field)


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
                    ]),
                    CurrentPasswordValidation(["sfa_secret"])
                ]
            )
        ),
        ("new_password", fld.PasswordField()),
        (
            "confirm_password",
            fld.PasswordField(validators=[vld.EqualTo("new_password")])
        ), (
            "sfa_secret",
            OTPSecretKeyField(qrcode_url="/u/qrcode", render_kw={
                "button_args": {"class": "btn"}
            }, validators=[
                ValidateTrue(
                    vld.InputRequired,
                    lambda form, field: form.sfa_confirm.data
                )
            ])
        ), (
            "sfa_confirm", fld.IntegerField(
                validators=[
                    ValidateTrue(
                        vld.Optional,
                        lambda form, field: not form.sfa_secret.data
                    ),
                    ValidateTrue(
                        vld.InputRequired,
                        lambda form, field: form.sfa_secret.data
                    ),
                    vld.NumberRange(min=0, max=999999),
                    OTPCheck(lambda form, field: form.sfa_secret.data)
                ]
            )
        )
    ])

    def on_model_change(self, form, model, is_created=False):
        """Apply new password."""
        password = form.current_password.data
        sfa_secret = form.sfa_secret.data or model.get_2fa(password)

        if form.confirm_password.data:
            model.password = form.confirm_password.data
            password = form.confirm_password.data

        model.set_2fa(password, sfa_secret)
