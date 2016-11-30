#!/usr/bin/env python
# coding=utf-8

"""User related forms like ContactForm."""

from django import forms as forms
from .models import Inbox


class ContactForm(forms.ModelForm):
    """Contact form."""

    class Meta(object):
        """Metadata."""

        model = Inbox
        exclude = ("user", "post_time")
