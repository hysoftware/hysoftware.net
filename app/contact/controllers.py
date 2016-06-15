#!/usr/bin/env python
# coding=utf-8

"""Contact controller."""

from urllib.parse import urljoin

import requests

from bson import ObjectId
from flask import make_response, jsonify, current_app, render_template
from flask.ext.classy import FlaskView
from .forms import ContactForm
from ..user.models import Person


class ContactView(FlaskView):
    """Contact controller."""

    trailing_slash = False

    def index(self):
        """GET request without model."""
        return render_template(
            "contact.html", model=Person.objects(),
            form=ContactForm()
        )

    def get(self, _id):
        """GET request."""
        return render_template(
            "contact.html", model=Person.objects(), active_id=_id,
            form=ContactForm()
        )

    def post(self):
        """POST request."""
        form = ContactForm()
        if not form.validate():
            return make_response(jsonify(form.errors), 417)
        person = Person.objects(id=ObjectId(form.to.data)).get()
        member_resp = requests.post(
            urljoin(current_app.config["MAILGUN_URL"] + "/", "messages"),
            auth=("api", current_app.config["MAILGUN_API"]),
            data={
                "from": form.email.data,
                "to": person.email,
                "subject": "Someone wants to contact you (hysoftware.net)",
                "text": render_template(
                    "mail_to_member.txt", form=form, member=person
                ),
                "html": render_template(
                    "mail_to_member.html", form=form, member=person
                )
            }
        )
        cli_resp = requests.post(
            urljoin(current_app.config["MAILGUN_URL"] + "/", "messages"),
            auth=("api", current_app.config["MAILGUN_API"]),
            data={
                "from": "HYSOFT Mailbot <noreply@hysoftware.net>",
                "to": form.email.data,
                "subject": "Thanks for your interest!",
                "text": render_template(
                    "mail_to_client.txt", form=form, member=person
                ),
                "html": render_template(
                    "mail_to_client.html", form=form, member=person
                )
            }
        )
        try:
            member_resp.raise_for_status()
            cli_resp.raise_for_status()
        except requests.HTTPError as e:
            return make_response(
                jsonify({"Mail": [e.response.json().get("message")]}),
                e.response.status_code
            )
        return ""
