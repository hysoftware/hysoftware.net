#!/usr/bin/env python
# coding=utf-8

"""User tasks."""

# import json
import requests
from celery import current_app
from django.conf import settings

from hysoftware_data.users import Users


@current_app.task(name="user.github.fetch")
def fetch_github_profile(user_info_id=None):
    """Fetch user profile from github."""
    users = Users(settings.NAME)
    if user_info_id is not None:
        users = [users[user_info_id]]

    for user in users:
        user.get_github_profile(disable_cache=True)


@current_app.task(name="user.mail")
def send_mail(mail_addr, title, html, txt, **kwargs):
    """Send a mail."""
    payload = {
        "from": kwargs.pop("from", settings.DEFAULT_FROM_EMAIL),
        "to": mail_addr,
        "subject": title,
        "html": html,
        "text": txt
    }
    requests.post(
        settings.MAILGUN_URL + "/messages",
        auth=("api", settings.MAILGUN_KEY), data=payload
    ).raise_for_status()
