#!/usr/bin/env python
# coding=utf-8

"""Email funcitonality tests."""

from unittest.mock import patch
from django.conf import settings
from django.test import TestCase

from app.user.tasks import send_mail


class MailTaskNameTest(TestCase):
    """Mail task name test."""

    def setUp(self):
        """Setup."""
        self.mail = send_mail

    def test_task_name(self):
        """The task name should be 'user.mail'."""
        self.assertEqual(self.mail.name, "user.mail")


class MailSendTest(TestCase):
    """Mail correctly send test."""

    def setUp(self):
        """Setup."""
        self.payload = {
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": "test@example.com",
            "subject": "This is a test title",
            "text": "Thie is a test message",
            "html": "<test>This is a test message.</test>"
        }
        self.mail = send_mail

    @patch("requests.post")
    def test_submit(self, post):
        """http.post should be called with proper payload."""
        self.mail(
            self.payload["to"], self.payload["subject"],
            self.payload["html"], self.payload["text"]
        )
        post.return_value.raise_for_status.assert_called_once_with()
        post.assert_called_once_with(
            settings.MAILGUN_URL + "/messages",
            auth=("api", settings.MAILGUN_KEY),
            data=self.payload
        )
