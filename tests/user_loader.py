#!/usr/bin/env python
# coding=utf-8

"""User load tests."""

import unittest as ut
from unittest.mock import patch, MagicMock

import app
import app.user.models as user


class UserLoadtest(ut.TestCase):
    """User load tests."""

    @patch("app.Person.objects")
    def test_user_load(self, objects):
        """Test user load."""
        test_user = user.Person(
            email="test@example.com", firstname="Test", lastname="Example"
        )
        objects.return_value.get = MagicMock(return_value=test_user)
        result = app.load_user(test_user.email)
        self.assertIs(result, test_user)
        objects.assert_called_once_with(pk=test_user.email)
        objects.return_value.get.assert_called_once_with()
