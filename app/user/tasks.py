#!/usr/bin/env python
# coding=utf-8

"""User tasks."""

import json
import requests
from celery import current_app
from django.contrib.auth import get_user_model
from django.conf import settings

from .models import UserInfo, GithubProfile, TaskLog


@current_app.task(name="user.github.fetch")
def fetch_github_profile(user_info_id=None):
    """Fetch user profile from github."""
    users_info_query = UserInfo.objects
    if user_info_id is not None:
        users_info_query = users_info_query.filter(id=user_info_id)

    for info in users_info_query.all():
        resp = requests.get(
            "https://api.github.com/users/%s" % info.github,
            headers={"Accept": "application/vnd.github.v3+json"},
            timeout=(10.0, 10.0)
        )
        try:
            resp.raise_for_status()
            GithubProfile.objects.update_or_create(
                user_info=info, defaults={
                    key: value
                    for (key, value) in resp.json().items()
                    if key in [
                        fld.name for fld in GithubProfile._meta.get_fields()
                        if fld.name != "id"
                    ]
                }
            )
            info.github_profile.refresh_from_db()
        except requests.HTTPError as e:
            TaskLog.objects.create(
                user=info.user, title="Github Profile Fetch Failed",
                message=(
                    "Fetching github profile failed because of "
                    "this error:\ncode:%d\nPayload: %s\nGithubID: %s"
                ) % (e.response.status_code, e.response.text, info.github)
            )


@current_app.task(name="user.mail")
def send_mail(mail_addr, title, html, txt):
    """Send a mail."""
    payload = {
        "from": settings.DEFAULT_FROM_EMAIL,
        "to": mail_addr,
        "subject": title,
        "html": html,
        "text": txt
    }
    resp = requests.post(
        settings.MAILGUN_URL + "/messages",
        auth=("api", settings.MAILGUN_KEY), json=payload
    )
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        msg = None
        user = get_user_model().objects.filter(email=mail_addr).first()
        try:
            msg = json.dumps(e.response.json(), indent=2)
        except json.JSONDecodeError:
            msg = e.response.text
        TaskLog.objects.create(
            user=user,
            title=("Mail Send Task Failure(To: {})").format(mail_addr),
            message=(
                "The mail couldn't be sent successfully. Here's the record. \n"
                "\nRequest Payload:\n{}\n\nResponse Code: {}\n"
                "Response Payload:\n{}"
            ).format(
                json.dumps(payload, indent=2), e.response.status_code,
                msg
            )
        )
