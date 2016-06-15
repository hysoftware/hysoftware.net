#!/usr/bin/env python
# coding=utf-8

"""Index rendering tests."""


from unittest import TestCase
from unittest.mock import patch

from flask.ext.login import current_user

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
