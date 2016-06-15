#!/usr/bin/env python
# coding=utf-8

"""Home rendering tests."""


from unittest import TestCase
from unittest.mock import patch, ANY

from app import app


class IndexRendering(TestCase):
    """Index rendering test case."""

    def setUp(self):
        """Setup function."""
        app.testing = True
        self.client = app.test_client()

    @patch("app.home.controllers.home.choice", return_value="test")
    @patch(
        "app.home.controllers.home.render_template",
        return_value="<body></body>"
    )
    def test_home_access(self, render_template, choice):
        """Should call render_template with home.html."""
        with self.client as cli:
            cli.get("/home")
            with cli.session_transaction() as session:
                self.assertEqual(session["tagline"], choice.return_value)
        render_template.assert_called_once_with(
            "home.html", tagline=choice.return_value, contact_form=ANY
        )
        self.assertTrue(choice.called)

    @patch("app.home.controllers.home.choice", return_value="test")
    @patch(
        "app.home.controllers.home.render_template",
        return_value="<body></body>"
    )
    def test_home_access_tagline_specified(self, render_template, choice):
        """Should call render_template with home.html."""
        with self.client as cli:
            with cli.session_transaction() as session:
                session["tagline"] = choice.return_value
            cli.get("/home")
            with cli.session_transaction() as session:
                self.assertEqual(session["tagline"], choice.return_value)
        render_template.assert_called_once_with(
            "home.html", tagline=choice.return_value,
            contact_form=ANY
        )
        choice.assert_not_called()
