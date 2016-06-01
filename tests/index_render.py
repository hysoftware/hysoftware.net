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
    @patch("app.home.controllers.index.minify_html")
    def test_index_access(self, minify, render_template, choice):
        """Should call render_template with index.html."""
        with self.client as cli:
            cli.get("/")
        render_template.assert_called_with(
            "index.html", tagline="Test tagline", minify=minify,
            current_user=current_user
        )
        self.assertTrue(choice.called)
