#!/usr/bin/env python
# coding=utf-8

"""Index rendering tests."""


from unittest import TestCase
from unittest.mock import patch

from flask_login import current_user

from app import app


class IndexRendering(TestCase):
    """Index rendering test case."""

    def setUp(self):
        """Setup function."""
        app.testing = True
        self.client = app.test_client()

    @patch("app.home.controllers.index.choice", return_value="Test tagline")
    @patch(
        "app.home.controllers.index.render_template",
        return_value="<body></body>"
    )
    def test_index_access(self, render_template, choice):
        """Should call render_template with index.html."""
        with self.client as cli:
            cli.get("/")
            with cli.session_transaction() as session:
                self.assertEqual(session["tagline"], choice.return_value)
        render_template.assert_called_once_with(
            "index.html", tagline=choice.return_value,
            current_user=current_user
        )
        self.assertTrue(choice.called)


class SSLValidation(TestCase):
    """SSL Validation test case."""

    def setUp(self):
        """Setup function."""
        app.testing = True
        self.client = app.test_client()

    @patch(
        "app.home.controllers.index.render_template",
        return_value="<body></body>"
    )
    def test_ssl_text_render(self, render_template):
        """the text for ssl validation should be rendered."""
        with self.client as cli:
            resp = cli.get("/ED512523231BF2C276F941231D7AC53D.txt")
            self.assertEqual(resp.status_code, 200)
        render_template.assert_called_once_with(
            "ED512523231BF2C276F941231D7AC53D.txt"
        )
