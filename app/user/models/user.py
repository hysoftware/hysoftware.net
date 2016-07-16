#!/usr/bin/env python
# coding=utf-8

"""User database."""

import bcrypt
from Crypto.Cipher import AES
from pyotp import TOTP
import flask_mongoengine as flskdb
import mongoengine as db
import mongoengine_goodjson as gj


class QuerySet(gj.QuerySet, flskdb.BaseQuerySet):
    """QuerySet."""

    pass


class Website(gj.EmbeddedDocument):
    """Website."""

    name = db.StringField(required=True, max_length=20)
    summary = db.StringField(required=True, max_length=140)
    page_class = db.StringField(max_length=20)
    url = db.URLField(required=True)


class Skill(gj.EmbeddedDocument):
    """Skill."""

    language = db.StringField(required=True, max_length=40)
    frameworks = db.ListField(db.EmbeddedDocumentField(Website))


class Person(gj.Document, flskdb.Document):
    """Person who is a part of hysoft."""

    meta = {"queryset_class": QuerySet}

    email = db.EmailField(unique=True, required=True)
    firstname = db.StringField(required=True)
    lastname = db.StringField(required=True)
    code = db.StringField(required=True, min_length=60, max_length=60)
    sacode = db.BinaryField()
    role = db.ListField(
        db.StringField(choices=[(item, item) for item in ["member", "admin"]]),
        required=True
    )
    title = db.StringField(max_length=40)
    bio = db.StringField()
    DOB = db.DateTimeField()
    DOD = db.DateTimeField()
    skills = db.ListField(db.EmbeddedDocumentField(Skill))
    websites = db.ListField(db.EmbeddedDocumentField(Website))
    is_authenticated = db.BooleanField(default=False)
    is_active = db.BooleanField(default=False)
    is_anonymous = False

    def get_id(self):
        """Return id."""
        return str(self.id)

    def verify(self, password, sfa_token=None):
        """Verify the password."""
        result = bcrypt.hashpw(
            password.encode(), self.code.encode()
        ) == self.code.encode()
        if self.sacode and result:
            otp = TOTP(self.get_2fa(password))
            result = result and otp.verify(sfa_token)
        return result

    @property
    def fullname(self):
        """Return full name."""
        return ("{} {}").format(self.firstname, self.lastname)

    @property
    def password(self):
        """Raise Value Error because password hash shouldn't be shown."""
        raise ValueError("Passowrd hash shouldn't be shown.")

    @password.setter
    def password(self, password):
        """Set the password."""
        self.code = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt(15)
        ).decode("utf-8")

    def set_2fa(self, password, fasecret):
        """Set 2FA secret key."""
        ec = AES.new(
            password[:32].ljust(32, "$").encode(), AES.MODE_CBC,
            password[::-1][:16].rjust(16, "#").encode()
        )
        self.sacode = ec.encrypt(fasecret)

    def get_2fa(self, password):
        """Get 2FA secret key."""
        ec = AES.new(
            password[:32].ljust(32, "$").encode(), AES.MODE_CBC,
            password[::-1][:16].rjust(16, "#").encode()
        )
        return ec.decrypt(self.sacode) if self.sacode else None
