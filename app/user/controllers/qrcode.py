#!/usr/bin/env python
# coding=utf-8

"""QRCode generation controller."""

from flask import abort, request, make_response
from flask_login import login_required, current_user
from flask_classy import FlaskView
from flask_wtf import Form
from wtf_otp import OTPSecretKeyField


class OTPDummyForm(Form):
    """Dummy form to generate the QR Code."""

    field = OTPSecretKeyField()


class QRCode(FlaskView):
    """QRCode controller."""

    trailing_slash = False
    decorators = [login_required]

    def index(self):
        """/qrcode get request."""
        secret = request.args.get("secret")
        if not secret:
            abort(404)
        form = OTPDummyForm()
        resp = make_response(form.field.qrcode(
            secret, name=current_user.email, issuer_name="HYSOFT"
        ))
        resp.mimetype = "image/svg+xml"
        return resp
