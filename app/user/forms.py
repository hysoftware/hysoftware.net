#!/usr/bin/env python
# coding=utf-8

"""User related forms like ContactForm."""

from django import forms as forms
from .models import Inbox
from captcha.fields import ReCaptchaField

from django_nghelp.forms import AngularForm
from django_nghelp.widgets import MDSelect


class ContactForm(AngularForm, forms.ModelForm):
    """Contact form."""

    class Meta(object):
        """Metadata."""

        name = "contactForm"
        model = Inbox
        exclude = ("post_time", )
        no_materialize = ("nobot", )
        no_label = ("nobot", )

        widgets = {
            "user": MDSelect(disable_select=True)
        }

    nobot = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        """Init the instance."""
        info_id = kwargs.pop("info_id", None)
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["user"].initial = info_id
