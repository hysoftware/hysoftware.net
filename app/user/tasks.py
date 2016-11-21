#!/usr/bin/env python
# coding=utf-8

"""User tasks."""

import requests
from celery import current_app

from .models import UserInfo, GithubProfile, TaskLog


@current_app.task(name="user.github.fetch")
def fetch_github_profile():
    """Fetch user profile from github."""
    users_info_query = UserInfo.objects

    for info in users_info_query.all():
        resp = requests.get(
            "https://api.github.com/users/%s" % info.github,
            headers={"Accept": "application/vnd.github.v3+json"},
            timeout=(10.0, 10.0)
        )
        try:
            resp.raise_for_status()
            GithubProfile.objects.update_or_create(
                user_info=info, **{
                    key: value
                    for (key, value) in resp.json().items()
                    if key in [
                        fld.name for fld in GithubProfile._meta.get_fields()
                        if fld.name != "id"
                    ]
                }
            )
        except requests.HTTPError as e:
            TaskLog.objects.create(
                user=info.user, title="Github Profile Fetch Failed",
                message=(
                    "Fetching github profile failed because of "
                    "this error:\ncode:%d\nPayload: %s\nGithubID: %s"
                ) % (e.response.status_code, e.response.text, info.github)
            )
