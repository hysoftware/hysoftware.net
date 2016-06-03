#!/usr/bin/env python
# coding=utf-8

"""Contact controller rendering tests."""

import json
from unittest import TestCase
from unittest.mock import patch, PropertyMock
from bson import ObjectId
# from flask.ext.mail import Message
from app import app, mail
from app.user.models import Person


class ContactSendingTest(TestCase):
    """Contact class test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        app.extensions["mail"].suppress = True
        self.cli = app.test_client()
        self.person = Person(id=ObjectId(), email="test@example.com")
        self.data = {
            "name": "Text Example",
            "to": self.person.get_id(),
            "company": "Test Corp.",
            "email": "test@example.com",
            "message": "This is a test."
        }

    def test_get(self):
        """[GET] Contact:index shouldn't be accessible."""
        with self.cli as cli:
            resp = cli.get("/contact")
            self.assertEqual(resp.status_code, 405)

    @patch("app.contact.controllers.Person.objects")
    @patch("app.contact.forms.Person.objects")
    @patch("app.contact.controllers.ContactForm")
    @patch("flask.ext.wtf.csrf.validate_csrf", return_value=True)
    def test_post(self, csrf, form, model, ctrl_model):
        """[POST] Contact:index should send email."""
        model.return_value = [self.person]
        ctrl_model.return_value.get.return_value = self.person
        form.return_value.validate.return_value = True
        for (key, value) in self.data.items():
            setattr(
                form.return_value, key, type("data", (object, ), {
                    "data": value
                })
            )
        with self.cli as cli:
            with mail.record_messages() as out:
                resp = cli.post("/contact", data=self.data)
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(len(out), 2)
        form.return_value.validate.assert_called_once_with()

    @patch("app.contact.controllers.Person.objects")
    @patch("app.contact.forms.Person.objects")
    @patch("app.contact.controllers.ContactForm")
    @patch("flask.ext.wtf.csrf.validate_csrf", return_value=True)
    def test_post_lacks_email(self, csrf, form, model, ctrl_model):
        """[POST] Contact:index should return 417 with an email error."""
        model.return_value = [self.person]
        form.return_value.validate.return_value = False
        errs = PropertyMock(
            return_value={"email": ["This field is required."]}
        )
        type(form.return_value).errors = errs
        with self.cli as cli:
            resp = cli.post("/contact")
            self.assertEqual(resp.status_code, 417)
            self.assertDictEqual(
                errs.return_value,
                json.loads(resp.data.decode("utf-8"))
            )
        form.return_value.validate.assert_called_once_with()
        errs.assert_called_once_with()
