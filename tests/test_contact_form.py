#!/usr/bin/env python
# coding=utf-8

"""ContactForm Tests."""

from unittest.mock import patch, call
from django.conf import settings
from django.test import TestCase

from hysoftware_data.users import Users

from app.user.forms import ContactForm


class ContactFormTest(TestCase):
    """Contact form test when info_id is specified."""

    def setUp(self):
        """Setup."""
        self.users = Users(settings.NAME)
        self.user = self.users[0]
        self.form = ContactForm({
            "user": str(self.user.id),
            "company_name": "Test Corp",
            "primary_name": "Test Name",
            "email": "test@example.com",
            "message": "This is a test",
            "g-recaptcha-response": "PASSED"
        })
        self.field = self.form.fields["user"]
        self.assertTrue(self.form.is_valid(), self.form.errors)

    def test_form(self):
        """The destination field should have inital value."""
        form = ContactForm(info_id=self.user.id)
        field = form.fields["user"]
        self.assertEqual(field.initial, self.user.id)

    @patch("app.user.forms.ctask")
    @patch("app.user.forms.loader")
    def test_save(self, loader, ctask):
        """Save function should send celery task asynchronously."""
        def render_to_string_side_effect(name, *args, **kwargs):
            """Get template side effect."""
            return "client_html" if name == "mail/client.html" \
                else "client_txt" if name == "mail/client.txt" \
                else "staff_html" if name == "mail/staff.html" \
                else "staff_txt" if name == "mail/staff.txt" \
                else None

        loader.render_to_string.side_effect = render_to_string_side_effect

        self.form.save()
        self.assertEqual(loader.render_to_string.call_count, 4)
        self.assertEqual(ctask.send_task.call_count, 2)
        staff_context = {
            "user": self.form.clean()["user"],
            "form": self.form
        }
        cli_context = {
            "form": self.form,
            "users_info": self.users
        }
        loader.render_to_string.assert_has_calls([
            call("mail/client.html", context=cli_context),
            call("mail/client.txt", context=cli_context),
            call("mail/staff.html", context=staff_context),
            call("mail/staff.txt", context=staff_context)
        ])
        ctask.send_task.assert_has_calls([
            call(
                "user.mail", (
                    self.form.clean()["email"],
                    "Thanks for your interest!",
                    "client_html", "client_txt"
                )
            ),
            call(
                "user.mail", (
                    self.user.email,
                    ("[{}] Someone wants you to contact him").format(
                        settings.TITLE
                    ),
                    "staff_html", "staff_txt"
                ), {"from": self.form.clean()["email"]}
            )
        ])
