#!/usr/bin/env python
# coding=utf-8

"""User related forms like ContactForm."""

from django import forms as forms
from .models import Inbox
from captcha.fields import ReCaptchaField

from django_nghelp.forms import AngularForm


class ContactForm(AngularForm, forms.ModelForm):
    """Contact form."""

    class Meta(object):
        """Metadata."""

        name = "contactForm"
        model = Inbox
        exclude = ("user", "post_time")
        no_materialize = ("nobot", )
        no_label = ("nobot", )

    nobot = ReCaptchaField()
