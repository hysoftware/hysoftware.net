#!/usr/bin/env python
# coding=utf-8

"""Admin password validation check."""

from unittest import TestCase
from unittest.mock import patch, MagicMock

from wtforms.form import Form
import wtforms.fields as fld
from werkzeug.datastructures import MultiDict

from app.user.admin import CurrentPasswordValidation
from app.user.models import Person


class TestForm(Form):
    """Test form."""

    email = fld.StringField()
    current_password = fld.PasswordField(
        validators=[CurrentPasswordValidation([
            "confirm_password", "new_password"
        ])]
    )
    new_password = fld.PasswordField()
    confirm_password = fld.PasswordField()


class ValidationTest(TestCase):
    """Successful validatoion tests."""

    def setUp(self):
        """Setup."""
        self.form = TestForm(MultiDict({
            "email": "test@example.com",
            "current_password": "test",
            "new_password": "test2",
            "confirm_password": "test3"
        }))

    @patch("app.user.admin.Person.objects")
    def test_none(self, person_objects):
        """Shouldn't raise anything."""
        person_objects.return_value.first.return_value = None
        self.assertTrue(self.form.validate())
        person_objects.return_value.first.assert_called_once_with()

    @patch("app.user.admin.Person.objects")
    def test_verification(self, person_objects):
        """Shouldn't raise anything."""
        person = Person(email="test@example.com")
        person.verify = MagicMock(return_value=True)
        person_objects.return_value.first.return_value = person
        self.assertTrue(self.form.validate())
        person_objects.return_value.first.assert_called_once_with()
        person.verify.assert_called_once_with(self.form.current_password.data)


class ValidationLacksConfirmPassword(TestCase):
    """Confirm passwrod lacks."""

    def setUp(self):
        """setup."""
        self.form = TestForm(MultiDict({
            "email": "test@example.com",
            "current_password": "test",
            "new_password": "test2"
        }))
        self.person = Person(email="test@example.com")
        self.person.verify = MagicMock()

    @patch("app.user.admin.Person.objects")
    def test_verification(self, person_objects):
        """Shouldn't raise anything."""
        person_objects.return_value.first.return_value = self.person
        self.assertTrue(self.form.validate())
        person_objects.return_value.first.assert_called_once_with()
        self.person.verify.assert_not_called()


class ValidationLacksNewPassword(TestCase):
    """New passwrod lacks."""

    def setUp(self):
        """setup."""
        self.form = TestForm(MultiDict({
            "email": "test@example.com",
            "current_password": "test",
            "confirm_password": "test2"
        }))
        self.person = Person(email="test@example.com")
        self.person.verify = MagicMock()

    @patch("app.user.admin.Person.objects")
    def test_verification(self, person_objects):
        """Shouldn't raise anything."""
        person_objects.return_value.first.return_value = self.person
        self.assertTrue(self.form.validate())
        person_objects.return_value.first.assert_called_once_with()
        self.person.verify.assert_not_called()


class ValidationLacksCurrentPassword(TestCase):
    """New passwrod lacks."""

    def setUp(self):
        """setup."""
        self.form = TestForm(MultiDict({
            "email": "test@example.com",
            "new_password": "test",
            "confirm_password": "test2"
        }))
        self.person = Person(email="test@example.com")
        self.person.verify = MagicMock()

    @patch("app.user.admin.Person.objects")
    def test_verification(self, person_objects):
        """Raise required error."""
        person_objects.return_value.first.return_value = self.person
        self.assertFalse(self.form.validate())
        self.assertDictEqual(
            {"current_password": ["This field is required."]},
            self.form.errors
        )
        person_objects.return_value.first.assert_called_once_with()
        self.person.verify.assert_not_called()


class ValidationCurrentPasswordNotMatch(TestCase):
    """New passwrod lacks."""

    def setUp(self):
        """setup."""
        self.form = TestForm(MultiDict({
            "email": "test@example.com",
            "current_password": "test0",
            "new_password": "test",
            "confirm_password": "test2"
        }))
        self.person = Person(email="test@example.com")
        self.person.verify = MagicMock(return_value=False)

    @patch("app.user.admin.Person.objects")
    def test_verification(self, person_objects):
        """Raise required error."""
        person_objects.return_value.first.return_value = self.person
        self.assertFalse(self.form.validate())
        self.assertDictEqual(
            {"current_password": ["The password wasn't matched."]},
            self.form.errors
        )
        person_objects.return_value.first.assert_called_once_with()
        self.person.verify.assert_called_once_with(
            self.form.current_password.data
        )
