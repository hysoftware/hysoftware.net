#!/usr/bin/env python
# coding=utf-8

"""Login template rendering tests."""

import unittest as ut
from unittest.mock import patch, ANY

from app import app


class LoginTemplateRenderingTest(ut.TestCase):
    """Login template should be rendered."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()

    @patch(
        "app.user.controllers.login.render_template",
        return_value="<body></body>"
    )
    def test_login_render(self, render_template):
        """Accessing /u/login, render_template should be called."""
        with self.cli as cli:
            resp = cli.get("/u/login")
            self.assertEqual(resp.status_code, 200)
        render_template.assert_called_once_with("login.html", form=ANY)
