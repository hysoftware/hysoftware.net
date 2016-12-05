#!/usr/bin/env python
# coding=utf-8

"""User related forms like ContactForm."""

from celery import current_app as ctask
from django import forms
from django.template import loader
from django.utils.translation import ugettext as _
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

        widgets = {"user": MDSelect()}

    nobot = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        """Init the instance."""
        info_id = kwargs.pop("info_id", None)
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["user"].initial = info_id

        for field in self.fields.values():
            field.widget.attrs.update({
                "data-ng-disabled": ("{}.$submitted").format(self.Meta.name)
            })

    def save(self):
        """Save the form."""
        super(ContactForm, self).save()
        ctask.send_task(
            "user.mail", (
                self.instance.email,
                _("Thanks for your interest!"),
                loader.get_template("mail/client.html").render(),
                loader.get_template("mail/client.txt").render()
            )
        )
        if self.instance.user.user.email:
            ctask.send_task(
                "user.mail", (
                    self.instance.user.user.email,
                    _("Someone is interested in you through hysoftware.net"),
                    loader.get_template("mail/staff.html").render(),
                    loader.get_template("mail/staff.txt").render()
                )
            )
