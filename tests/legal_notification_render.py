#!/usr/bin/env python
# coding=utf-8

"""Legal Notificaiton Rendering test."""

from unittest import TestCase
from unittest.mock import patch, ANY

from app import app
from app.about.controllers import LegalView


class LegalNotationRenderingTest(TestCase):
    """
    Legal Notification Rendering test.

    I found Japan has weird Law named "Specified Commercial Transaction Act".
    I'm not sure if this law really works in these days, but the law is law.
    """

    def setUp(self):
        """Setup the function."""
        app.testing = True
        self.client = app.test_client()

    @patch(
        "app.about.controllers.legal.render_template",
        return_value="<body></body>"
    )
    def test_about_rendering(self, render_template):
        """The legal notification should be rendered."""
        with self.client as cli:
            resp = cli.get("/about/legal")
            self.assertEqual(resp.status_code, 200)
        render_template.assert_called_once_with(
            "legal.html", regulations=LegalView.regulations,
            assets_info=ANY
        )
