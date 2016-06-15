#!/usr/bin/env python
# coding=utf-8

"""About page rendering tests."""

from unittest import TestCase
from unittest.mock import patch

from app import app


class AboutPageRenderingTest(TestCase):
    """About page rendering test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()

    @patch(
        "app.about.controllers.team.render_template",
        return_value="<body></body>"
    )
    @patch("app.about.controllers.team.Person.objects")
    def test_rendering(self, person, render):
        """GETting /about/team, render_template should be called."""
        with self.cli as cli:
            resp = cli.get("/about")
            self.assertEqual(resp.status_code, 200)
        render.assert_called_once_with("team.html", model=person.return_value)
        person.assert_called_once_with(role__in=["member"])
