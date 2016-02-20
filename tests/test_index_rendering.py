#!/usr/bin/env python
# coding=utf-8


from unittest import TestCase
from unittest.mock import patch

class IndexRendering(TestCase):
    '''
    Index rendering test case
    '''

    @patch("random.choice", return_value="Test tagline")
    @patch("flask.render_template", return_value="")
    def setUp(self, render_template, random_choice):
        from app import app
        app.testing = True
        self.client = app.test_client()
        self.render_template = render_template
        self.random_choice = random_choice

    def test_index_access(self):
        '''
        self.render_template should be called with index.html
        '''
        with self.client as cli:
            cli.get("/")
        self.render_template.assert_called_with(
            "index.html", tagline="Test tagline"
        )
        assert self.random_choice.called
