#!/usr/bin/env python
# coding=utf-8

"""Contact controller rendering tests."""

import json
from urllib.parse import urljoin
from unittest import TestCase
from unittest.mock import patch, PropertyMock, call, ANY
from bson import ObjectId
from app import app
from app.user.models import Person


class ContactSendingTest(TestCase):
    """Contact class test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()
        self.person = Person(
            id=ObjectId(), email="test@example.com",
            firstname="Test", lastname="Person"
        )
        self.url = urljoin(app.config["MAILGUN_URL"] + "/", "messages")
        self.auth = ("api", app.config["MAILGUN_API"])
        self.data = {
            "name": "Text Example",
            "to": self.person.get_id(),
            "company": "Test Corp.",
            "email": "test@example.com",
            "message": "This is a test."
        }

    @patch("requests.post")
    @patch("app.contact.controllers.render_template")
    @patch("app.contact.controllers.Person.objects")
    @patch("app.contact.forms.Person.objects")
    @patch("app.contact.controllers.ContactForm")
    @patch("flask.ext.wtf.csrf.validate_csrf", return_value=True)
    def test_post(self, csrf, form, model, ctrl_model, render_template, post):
        """[POST] Contact:index should send email."""
        def render_template_side_effect(f, **kwargs):
            return {
                "mail_to_member.txt": "member.txt",
                "mail_to_member.html": "member.html",
                "mail_to_client.txt": "client.txt",
                "mail_to_client.html": "client.html"
            }[f]
        render_template.side_effect = render_template_side_effect

        model.return_value = [self.person]
        ctrl_model.return_value.get.return_value = self.person
        form.return_value.validate.return_value = True
        for (key, value) in self.data.items():
            setattr(form.return_value, key, type("data", (object, ), {
                "data": value
            }))
        with self.cli as cli:
            resp = cli.post("/contact", data=self.data)
            self.assertEqual(resp.status_code, 200)
        self.assertEqual(post.call_count, 2)
        post.assert_has_calls([
            call(self.url, auth=self.auth, data={
                "from": self.data["email"],
                "to": self.person.email,
                "subject": (
                    "Someone wants to contact you (hysoftware.net)"
                ).format(self.data["name"]),
                "text": render_template.side_effect("mail_to_member.txt"),
                "html": render_template.side_effect("mail_to_member.html")
            }),
            call(self.url, auth=self.auth, data={
                "from": "HYSOFT Mailbot <noreply@hysoftware.net>",
                "to": self.data["email"],
                "subject": "Thanks for your interest!",
                "text": render_template.side_effect("mail_to_client.txt"),
                "html": render_template.side_effect("mail_to_client.html")
            })
        ], any_order=True)
        form.return_value.validate.assert_called_once_with()

    @patch("requests.post")
    @patch("app.contact.controllers.Person.objects")
    @patch("app.contact.forms.Person.objects")
    @patch("app.contact.controllers.ContactForm")
    @patch("flask.ext.wtf.csrf.validate_csrf", return_value=True)
    def test_post_lacks_email(self, csrf, form, model, ctrl_model, post):
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
        post.assert_not_called()
        form.return_value.validate.assert_called_once_with()
        errs.assert_called_once_with()


class ContactGETTest(TestCase):
    """Contact GET request test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()
        self.models = [Person(id=ObjectId())]
        self.select = self.models[0].get_id()

    @patch(
        "app.contact.controllers.render_template",
        return_value="<body><body>"
    )
    @patch("app.contact.controllers.Person.objects")
    def test_index_rendering(self, objects, render_template):
        """Getting /contact, render_template should be read properly."""
        objects.return_value = self.models
        with self.cli as cli:
            resp = cli.get("/contact")
            self.assertEqual(resp.status_code, 200)
        objects.assert_called_once_with()
        render_template.assert_called_once_with(
            "contact.html", model=objects.return_value, form=ANY
        )

    @patch(
        "app.contact.controllers.render_template",
        return_value="<body><body>"
    )
    @patch("app.contact.controllers.Person.objects")
    def test_get_rendering(self, objects, render_template):
        """Getting /contact/:id, render_template should be read properly."""
        objects.return_value = self.models
        with self.cli as cli:
            resp = cli.get(("/contact/{}").format(self.select))
            self.assertEqual(resp.status_code, 200)
        objects.assert_called_once_with()
        render_template.assert_called_once_with(
            "contact.html", model=objects.return_value,
            active_id=self.select, form=ANY
        )
