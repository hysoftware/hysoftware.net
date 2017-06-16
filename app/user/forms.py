#!/usr/bin/env python
# coding=utf-8

"""User related forms like ContactForm."""

from celery import current_app as ctask
from django import forms
from django.conf import settings
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

    nobot = ReCaptchaField(attrs={
        "callback": "recaptchaCallback",
        "size": "invisible",
        "badge": "inline"
    })

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
        cli_context = {
            "form": self,
            "users_info": self.Meta.model._meta.get_field("user").model.objects
        }
        ctask.send_task(
            "user.mail", (
                self.instance.email,
                _("Thanks for your interest!"),
                loader.render_to_string(
                    "mail/client.html", context=cli_context
                ),
                loader.render_to_string("mail/client.txt", context=cli_context)
            )
        )
        if self.instance.user.user.email:
            context = {
                "user": self.instance.user.user,
                "form": self
            }
            ctask.send_task(
                "user.mail", (
                    self.instance.user.user.email,
                    _("[{}] Someone wants you to contact him").format(
                        settings.TITLE
                    ),
                    loader.render_to_string(
                        "mail/staff.html", context=context
                    ),
                    loader.render_to_string("mail/staff.txt", context=context)
                ), {"from": self.instance.email}
            )
