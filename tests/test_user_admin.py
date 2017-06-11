#!/usr/bin/env python
# coding=utf-8

"""User admin tests."""

import uuid
from unittest.mock import patch, MagicMock

from django.contrib.auth import get_user_model
from django.test import TestCase

from app.user.models import UserInfo
from app.user.admin import UserInfoAdmin


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

    @patch("app.user.admin.fetch_github_profile")
    def test_task_send(self, fetch_github_profile):
        """Should call fetch_github_profile."""
        obj = MagicMock()
        obj.id = uuid.uuid4
        self.admin.save_model(None, obj, None, None)
        fetch_github_profile.assert_called_once_with(str(obj.id))
