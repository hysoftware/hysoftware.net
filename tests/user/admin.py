#!/usr/bin/env python
# coding=utf-8

"""User Admin Panel tests."""

from unittest import TestCase
from unittest.mock import patch, PropertyMock, MagicMock

from wtforms.form import Form
import wtforms.fields as fld
from wtf_otp import OTPSecretKeyField
from werkzeug.datastructures import MultiDict

from app.user.models import Person
from app.user.admin import PersonAdmin


class TestForm(Form):
    """Test form."""

    current_password = fld.PasswordField()
    confirm_password = fld.PasswordField()
    sfa_secret = OTPSecretKeyField()
    sfa_confirm = fld.IntegerField()


class PersonAdminEmptyConfirmPasswordTest(TestCase):
    """Test case that confirm password is empty."""

    def setUp(self):
        """Setup."""
        self.form = TestForm()
        self.person = Person()
        self.person.get_2fa = MagicMock(return_value="")
        self.person.set_2fa = MagicMock(return_value="")
        self.admin = PersonAdmin(Person)

    @patch("app.user.admin.Person.password", new_callable=PropertyMock)
    def test_password_not_called(self, pw):
        """Password property not called."""
        self.admin.on_model_change(self.form, self.person)
        pw.assert_not_called()


class PersonAdminNonEmptyConfirmPasswordTest(TestCase):
    """Test case that confirm password is not empty."""

    def setUp(self):
        """Setup."""
        self.form = TestForm(MultiDict({"confirm_password": "test"}))
        self.person = Person()
        self.person.get_2fa = MagicMock(return_value="")
        self.person.set_2fa = MagicMock(return_value="")
        self.admin = PersonAdmin(Person)

    @patch("app.user.admin.Person.password", new_callable=PropertyMock)
    def test_password_not_called(self, pw):
        """Password property should be called with confirm_password."""
        self.admin.on_model_change(self.form, self.person)
        pw.assert_called_once_with(self.form.confirm_password.data)
