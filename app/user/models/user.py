#!/usr/bin/env python
# coding=utf-8

"""User database."""

import mongoengine as db
import bcrypt


class Website(db.EmbeddedDocument):
    """Website."""

    name = db.StringField(required=True)
    summary = db.StringField(required=True, max_length=400)
    page_class = db.StringField(required=True)
    url = db.URLField(required=True)


class Skill(db.EmbeddedDocument):
    """Skill."""

    language = db.StringField(required=True)
    frameworks = db.EmbeddedDocumentListField(Website)


class Person(db.Document):
    """Person who is a part of hysoft."""

    email = db.EmailField(primary_key=True)
    firstname = db.StringField(required=True)
    lastname = db.StringField(required=True)
    code = db.StringField(required=True, min_length=60, max_length=60)
    role = db.ListField(
        db.StringField(
            choices=[(item, item) for item in [
                "normal", "admin", "developer"
            ]]
        ),
        required=True
    )
    DOB = db.DateTimeField()
    DOD = db.DateTimeField()
    skills = db.EmbeddedDocumentListField(Skill)
    websites = db.EmbeddedDocumentListField(Website)
    is_authenticated = db.BooleanField(required=True, default=False)
    is_active = db.BooleanField(Required=True, default=False)
    is_anonymous = False

    def get_id(self):
        """Return id."""
        return str(self.id)

    def verify(self, password):
        """Verify the password."""
        return bcrypt.hashpw(
            password.encode(), self.code.encode()
        ) == self.code.encode()

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
