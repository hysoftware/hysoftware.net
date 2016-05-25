#!/usr/bin/env python
# coding=utf-8

"""User Model tests."""

import unittest as ut
from unittest.mock import patch

import app.user.models as user_models


class PasswordHashTestBase(ut.TestCase):
    """Password Hash Test Base."""

    def setUp(self):
        """setup."""
        self.model = user_models.Person(
            email="test@example.com",
            firstname="Test", lastname="Example",
            code=("$2b$14$c5EPH.uYkcELops3BI1."
                  "/O6jkqkKhwSuDRbgEBCSYvhjroIys0EPm"),
            role=["normal"]
        )


class PasswordHashReadTest(PasswordHashTestBase):
    """Password Hash Read Test."""

    def test_password_not_read_directly(self):
        """The password hash shouldn't be read directly."""
        with self.assertRaises(ValueError) as e:
            self.model.password

        self.assertEqual(
            str(e.exception), "Passowrd hash shouldn't be shown."
        )


class PasswordVerificationTest(PasswordHashTestBase):
    """Password Hash Read Test."""

    @patch("bcrypt.hashpw")
    @patch("bcrypt.gensalt")
    def test_verify(self, gensalt, hashpw):
        """Verify should work properly."""
        data = "This is a test."
        hashpw.return_value = self.model.code.encode()
        result = self.model.verify(data)
        self.assertTrue(result)
        hashpw.assert_called_once_with(data.encode(), self.model.code.encode())
        gensalt.assert_not_called()


class PasswordWriteTest(PasswordHashTestBase):
    """Password hash write test."""

    @patch("bcrypt.hashpw")
    @patch("bcrypt.gensalt")
    def test_generate(self, gensalt, hashpw):
        """self.model.password = [???] should work correctly."""
        data = "Hello World"
        hashpw.return_value = b"Success!"
        gensalt.return_value = b"Salt Generation Success"
        self.model.password = data
        hashpw.assert_called_once_with(data.encode(), gensalt.return_value)
        gensalt.assert_called_once_with(15)
        self.assertEqual(self.model.code, hashpw.return_value.decode("utf-8"))
