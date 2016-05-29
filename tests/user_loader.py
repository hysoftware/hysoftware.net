#!/usr/bin/env python
# coding=utf-8

"""User load tests."""

import unittest as ut
from bson import ObjectId
from unittest.mock import patch, MagicMock

import app
import app.user.models as user


class UserLoadtest(ut.TestCase):
    """User load tests."""

    @patch("app.Person.objects")
    def test_user_load(self, objects):
        """Test user load."""
        test_user = user.Person(
            id=ObjectId(),
            email="test@example.com",
            firstname="Test", lastname="Example"
        )
        objects.return_value.get = MagicMock(return_value=test_user)
        result = app.load_user(test_user.id)
        self.assertIs(result, test_user)
        objects.assert_called_once_with(pk=test_user.id)
        objects.return_value.get.assert_called_once_with()

    @patch("app.Person.objects", side_effect=[user.Person.DoesNotExist])
    def test_user_not_found(self, objects):
        """Don't throw DoesNotExist if the document didn't found."""
        test_user = user.Person(
            id=ObjectId(),
            email="test@example.com",
            firstname="Test", lastname="Example"
        )
        result = app.load_user(test_user.id)
        self.assertIsNone(result)
