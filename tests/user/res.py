#!/usr/bin/env python
# coding=utf-8

"""Login resource rendering tests."""

import unittest as ut
from unittest.mock import patch, ANY

from app import app
import app.user.models as user


class LoginIndexTest(ut.TestCase):
    """GET Login resource should be generated."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()

    @patch(
        "app.user.controllers.login.render_template",
        return_value="<body></body>"
    )
    def test_login_render(self, render_template):
        """GETting /u/login, render_template should be called."""
        with self.cli as cli:
            resp = cli.get("/u/login")
            self.assertEqual(resp.status_code, 200)
        render_template.assert_called_once_with("login.html", form=ANY)


class LoginPostTest(ut.TestCase):
    """POST login test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        app.config["WTF_CSRF_ENABLED"] = not app.testing
        app.config["WTF_CSRF_CHECK_DEFAULT"] = app.config["WTF_CSRF_ENABLED"]
        self.cli = app.test_client()

    @patch("app.user.models.Person.objects.get_or_404")
    @patch("app.user.models.Person.verify", return_value=True)
    def test_post_login(self, get_or_404, verify):
        """
        Test POST /u/login.

        POSTing /u/login, the GETting /u/status, proper user should be shown.
        """
        import json
        person = user.Person(email="test@example.com")
        get_or_404.return_value = person
        user_status = None
        with self.cli as cli:
            post_resp = cli.post("/u/login", data=json.dumps({
                "email": "test@example.com",
                "passowrd": "test"
            }))
            self.assertEqual(post_resp.status_code, 200)
            get_resp = cli.get("/u/login/status")
            self.assertEqual(get_resp.status_code, 200)
            user_status = get_resp.data
        self.assertEqual(user_status["email"], person.email)
