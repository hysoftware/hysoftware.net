#!/usr/bin/env python
# coding=utf-8


from unittest import TestCase
from unittest.mock import patch
from app import app


class IndexRendering(TestCase):
    '''
    Index rendering test case
    '''

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch("app.home.controller.choice", return_value="Test tagline")
    @patch(
        "app.home.controller.render_template",
        return_value="<body></body>"
    )
    def test_index_access(self, render_template, choice):
        '''
        self.render_template should be called with index.html
        '''
        with self.client as cli:
            cli.get("/")
        render_template.assert_called_with(
            "index.html", tagline="Test tagline"
        )
        self.assertTrue(choice.called)
