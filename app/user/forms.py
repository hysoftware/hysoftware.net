#!/usr/bin/env python
# coding=utf-8

"""User related forms like ContactForm."""

from celery import current_app as ctask
from django import forms
from django.conf import settings
from django.template import loader
from django.utils.translation import ugettext as _, ugettext_lazy as _lz
from captcha.fields import ReCaptchaField

from django_nghelp.forms import AngularForm
from django_nghelp.widgets import MDSelect

from hysoftware_data.users import Users


class ContactForm(AngularForm):
    """Contact form."""

    class Meta(object):
        """Metadata."""

        name = "contactForm"
        no_materialize = ("nobot", )
        no_label = ("nobot", )

    instances = Users(settings.NAME)
    user = forms.TypedChoiceField(
        widget=MDSelect(),
        choices=[
            (item.id, ("{} {}").format(item.first_name, item.last_name))
            for item in instances
        ]
    )
    primary_name = forms.CharField(label=_lz("Your Name"), max_length=40)
    email = forms.EmailField()
    company_name = forms.CharField(max_length=40)
    message = forms.CharField(widget=forms.Textarea)
    nobot = ReCaptchaField(attrs={
        "callback": "recaptchaCallback",
        "size": "invisible",
        "badge": "inline"
    })

    def __init__(self, *args, **kwargs):
        """Init the instance."""
        info_id = kwargs.pop("info_id", None)
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["user"].coerce = lambda value: self.instances[value]
        self.fields["user"].initial = info_id

        for field in self.fields.values():
            field.widget.attrs.update({
                "data-ng-disabled": ("{}.$submitted").format(self.Meta.name)
            })

    def save(self):
        """Save the form."""
        user = self.clean()["user"]
        cli_context = {
            "form": self,
            "users_info": self.instances
        }
        ctask.send_task(
            "user.mail", (
                self.clean()["email"],
                _("Thanks for your interest!"),
                loader.render_to_string(
                    "mail/client.html", context=cli_context
                ),
                loader.render_to_string("mail/client.txt", context=cli_context)
            )
        )
        context = {
            "user": user,
            "form": self
        }
        ctask.send_task(
            "user.mail", (
                user.email,
                _("[{}] Someone wants you to contact him").format(
                    settings.TITLE
                ),
                loader.render_to_string(
                    "mail/staff.html", context=context
                ),
                loader.render_to_string("mail/staff.txt", context=context)
            ), {"from": self.clean()["email"]}
        )
