#!/usr/bin/env python
# coding=utf-8


from unittest import TestCase
from unittest.mock import patch

class IndexRendering(TestCase):
    '''
    Index rendering test case
    '''

    @patch("flask.render_template", return_value="")
    def setUp(self, mock):
        from app import app
        app.testing = True
        self.client = app.test_client()
        self.render_template = mock

    def test_index_access(self):
        '''
        self.render_template should be called with index.html
        '''
        with self.client as cli:
            cli.get("/")
        print(self.render_template)
        self.render_template.assert_called_with("index.html")
