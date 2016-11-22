#!/usr/bin/env python
# coding=utf-8

"""User admin tests."""

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

    @patch("app.user.admin.ctask")
    def test_task_send(self, ctask):
        """Celery should send task to fetch github profile."""
        obj = MagicMock()
        self.admin.save_model(None, obj, None, None)
        ctask.send_task.assert_called_once_with(
            "user.github.fetch", (obj.id,)
        )
