#!/usr/bin/env python
# coding=utf-8

"""User admin tests."""

import uuid
from unittest.mock import patch, MagicMock

from django.contrib.auth import get_user_model
from django.test import TestCase

from app.user.models import UserInfo
from app.user.admin import UserInfoAdmin
from app.user.tasks import fetch_github_profile


class GithubTaskSendTest(TestCase):
    """Github task sending test on save."""

    def setUp(self):
        """Setup."""
        self.user = get_user_model().objects.create_user(
            username="Test", password="test"
        )
        self.user_info = UserInfo.objects.create(
            user=self.user, github="octocat"
        )
        self.admin = UserInfoAdmin(self.user_info, None)

    @patch("app.user.admin.zappa_async")
    def test_task_send(self, zappa_async):
        """zappa_async should send task to fetch github profile."""
        obj = MagicMock()
        obj.id = uuid.uuid4
        self.admin.save_model(None, obj, None, None)
        zappa_async.run(fetch_github_profile, (str(obj.id),))
