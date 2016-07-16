#!/usr/bin/env python
# coding=utf-8

"""User Model tests."""

import random
import unittest as ut
from unittest.mock import patch, MagicMock

from Crypto.Cipher import AES

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
        """Verify should call hashpw."""
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


class SFAVerifyTest(PasswordHashTestBase):
    """Password verification with 2FA test."""

    def setUp(self):
        """Setup."""
        super().setUp()
        self.model.sacode = b"testtesttesttest"
        self.model.get_2fa = MagicMock()

    @patch("bcrypt.hashpw")
    @patch("app.user.models.user.TOTP")
    def test_2fa(self, OTP, hashpw):
        """Test OTP token should be checked when sacode is truthy value."""
        hashpw.return_value = self.model.code.encode()
        OTP.return_value.verify.return_value = True
        token = random.randint(0, 999999)
        self.assertTrue(self.model.verify("test", token))
        OTP.assert_called_once_with(self.model.get_2fa.return_value)
        OTP.return_value.verify.assert_called_once_with(token)

    @patch("bcrypt.hashpw")
    @patch("app.user.models.user.TOTP")
    def test_2fa_without_token(self, OTP, hashpw):
        """Test OTP token should be checked even if token is not set."""
        hashpw.return_value = self.model.code.encode()
        OTP.return_value.verify.return_value = False
        self.assertFalse(self.model.verify("test"))
        OTP.assert_called_once_with(self.model.get_2fa.return_value)
        OTP.return_value.verify.assert_called_once_with(None)


class IDCheck(PasswordHashTestBase):
    """The return value from get_id should be equal to str(model.id)."""

    def test_id(self):
        """The return value from get_id should be equal to str(model.id)."""
        self.assertEqual(self.model.get_id(), str(self.model.id))


class FullName(ut.TestCase):
    """Test full name property."""

    def setUp(self):
        """setup."""
        self.person = user_models.Person(firstname="Test", lastname="Example")

    def test_fullname(self):
        """Accessing fullname property, returns "Test Example"."""
        self.assertEqual(self.person.fullname, "Test Example")


class TwoFAStoreTest(ut.TestCase):
    """2FA store test."""

    def setUp(self):
        """setup."""
        self.person = user_models.Person(firstname="Test", lastname="Example")
        self.secret_key = "This is a test"
        self.person.sacode = b"This is a test"
        self.twofasacret = "23456789ABCDEFGH"

    @patch("app.user.models.user.AES.new")
    def test_set(self, aes_new):
        """AES256 should be initialized and it encrypts the data."""
        aes_new.return_value.encrypt.return_value = b"testesttest"
        self.person.set_2fa(self.secret_key, self.twofasacret)
        aes_new.assert_called_once_with(
            self.secret_key[:32].ljust(32, "$").encode(),
            AES.MODE_CBC, self.secret_key[::-1][:16].rjust(16, "#").encode()
        )
        aes_new.return_value.encrypt.assert_called_once_with(self.twofasacret)
        self.assertIs(
            self.person.sacode, aes_new.return_value.encrypt.return_value
        )

    @patch("app.user.models.user.AES.new")
    def test_get(self, aes_new):
        """AES256 should be initialized and it decodes the data."""
        ret = self.person.get_2fa(self.secret_key)
        aes_new.assert_called_once_with(
            self.secret_key[:32].ljust(32, "$").encode(),
            AES.MODE_CBC, self.secret_key[::-1][:16].rjust(16, "#").encode()
        )
        aes_new.return_value.decrypt.assert_called_once_with(
            self.person.sacode
        )
        self.assertIs(
            ret, aes_new.return_value.decrypt.return_value
        )
