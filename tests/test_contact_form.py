#!/usr/bin/env python
# coding=utf-8

"""ContactForm Tests."""

import uuid
from django.test import TestCase

from app.user.forms import ContactForm


class ContactFormInitTest(TestCase):
    """Contact form test when info_id is specified."""

    def test_form(self):
        """The destination field should have inital value."""
        info_id = uuid.uuid4()
        form = ContactForm(info_id=info_id)
        field = form.fields["user"]
        self.assertEqual(field.initial, info_id)
