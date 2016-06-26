#!/usr/bin/env python
# coding=utf-8

"""Font Rendering Tests."""

from unittest import TestCase
from unittest.mock import patch

from app import app
from app.fonts.controller import OpenSansView


class OpenSansFontsRenderingTests(TestCase):
    """Open Sans font rendering tests."""

    def setUp(self):
        """Setup the function."""
        app.testing = True
        self.cli = app.test_client()

    @patch(
        "app.fonts.controller.render_template",
        return_value="<body></body>"
    )
    def test_fontface_rendering(self, render_template):
        """font-face should be rendered."""
        with self.cli as cli:
            resp = cli.get("/fonts/opensans")
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.mimetype, "text/css")

        render_template.assert_called_once_with(
            "opensans.css", unicode_range=OpenSansView.unicode_range
        )
