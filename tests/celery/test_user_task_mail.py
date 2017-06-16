#!/usr/bin/env python
# coding=utf-8

"""Email funcitonality tests."""

import io
import json

from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.conf import settings
from django.test import TestCase
import requests

from app.user.tasks import send_mail
from app.user.models import TaskLog


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


class MailSendErrorTestWithoutUser(TestCase):
    """Mail send error test without user."""

    def setUp(self):
        """Setup."""
        if not getattr(self, "payload", None):
            self.payload = {
                "from": settings.DEFAULT_FROM_EMAIL,
                "to": "test@example.com",
                "subject": "This is a test title",
                "text": "Thie is a test message",
                "html": "<test>This is a test message.</test>"
            }
        self.mail = send_mail
        req = requests.Request("POST", settings.MAILGUN_URL, data=self.payload)
        self.resp = requests.Response()
        self.resp.status_code = 417
        self.resp.headers["Content-Type"] = "application/json"
        self.resp.raw = io.BytesIO(
            json.dumps({"error": "this is the error message"}).encode()
        )
        self.resp.encoding = "utf-8"
        self.resp.reason = "Expectation Failed"
        self.resp.request = req

    @patch("requests.post")
    def test_log_user(self, post):
        """The tasklog shouldn't have user model."""
        post.return_value.raise_for_status.side_effect = \
            requests.HTTPError(response=self.resp)
        self.mail(
            self.payload["to"], self.payload["subject"],
            self.payload["html"], self.payload["text"]
        )
        log = TaskLog.objects.get()
        self.assertIsNone(log.user)

    @patch("requests.post")
    @patch("json.dumps")
    def test_log_title_message(self, dumps, post):
        """If the request raises an error, the error should be logged it."""
        def dumps_side_effect(dct, **kwargs):
            return "payload" if dct == self.payload \
                else "response" if dct == self.resp.json() else None
        dumps.side_effect = dumps_side_effect
        post.return_value.raise_for_status.side_effect = \
            requests.HTTPError(response=self.resp)
        self.mail(
            self.payload["to"], self.payload["subject"],
            self.payload["html"], self.payload["text"]
        )

        log = TaskLog.objects.get()
        self.assertEqual(
            log.title,
            ("Mail Send Task Failure(To: {})").format(self.payload["to"])
        )
        self.assertEqual(
            log.message,
            (
                "The mail couldn't be sent successfully. Here's the record. \n"
                "\nRequest Payload:\n{}\n\nResponse Code: {}\n"
                "Response Payload:\n{}"
            ).format(
                json.dumps(self.payload), self.resp.status_code,
                json.dumps(self.resp.json())
            )
        )


class MailSendErrorTestWithUser(MailSendErrorTestWithoutUser):
    """Mail send error test without user."""

    def setUp(self):
        """Setup."""
        self.user = get_user_model().objects.create_user(
            username="test", password="test", email="test@example.com"
        )
        self.payload = {
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": "test@example.com",
            "subject": "This is a test title",
            "text": "Thie is a test message",
            "html": "<test>This is a test message.</test>"
        }
        super(MailSendErrorTestWithUser, self).setUp()

    @patch("requests.post")
    def test_log_user(self, post):
        """The tasklog should have user model."""
        post.return_value.raise_for_status.side_effect = \
            requests.HTTPError(response=self.resp)
        self.mail(
            self.payload["to"], self.payload["subject"],
            self.payload["html"], self.payload["text"]
        )
        log = TaskLog.objects.get()
        self.assertEqual(log.user, self.user)


class MailSendErrorPlainTextTest(MailSendErrorTestWithoutUser):
    """Mail send error test with plain text."""

    def setUp(self):
        """Setup."""
        super(MailSendErrorPlainTextTest, self).setUp()
        self.resp.headers["Content-Type"] = "text/plain"
        self.resp.raw = io.BytesIO(("This is a test meessage").encode())

    @patch("requests.post")
    @patch("json.dumps")
    def test_log_title_message(self, dumps, post):
        """If the request raises an error, the error should be logged it."""
        def dumps_side_effect(dct, **kwargs):
            return "payload" if dct == self.payload \
                else "response" if dct == self.resp.json() else None
        dumps.side_effect = dumps_side_effect
        post.return_value.raise_for_status.side_effect = \
            requests.HTTPError(response=self.resp)
        self.mail(
            self.payload["to"], self.payload["subject"],
            self.payload["html"], self.payload["text"]
        )

        log = TaskLog.objects.get()
        self.assertIsNone(log.user)
        self.assertEqual(
            log.title,
            ("Mail Send Task Failure(To: {})").format(self.payload["to"])
        )
        self.assertEqual(
            log.message,
            (
                "The mail couldn't be sent successfully. Here's the record. \n"
                "\nRequest Payload:\n{}\n\nResponse Code: {}\n"
                "Response Payload:\n{}"
            ).format(
                json.dumps(self.payload), self.resp.status_code,
                self.resp.text
            )
        )
