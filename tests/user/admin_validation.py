#!/usr/bin/env python
# coding=utf-8

"""Admin validation checks."""

from unittest import TestCase
from unittest.mock import patch, MagicMock

from wtforms.form import Form
import wtforms.fields as fld
from werkzeug.datastructures import MultiDict

from app.user.admin import CurrentPasswordValidation, ValidateTrue
from app.user.models import Person


class CurrentPasswordTestForm(Form):
    """Test form."""

    email = fld.StringField()
    current_password = fld.PasswordField(
        validators=[CurrentPasswordValidation([
            "confirm_password", "new_password"
        ])]
    )
    new_password = fld.PasswordField()
    confirm_password = fld.PasswordField()


class CurrentPasswordValidationTest(TestCase):
    """Successful validatoion tests."""

    def setUp(self):
        """Setup."""
        self.form = CurrentPasswordTestForm(MultiDict({
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


class CurrentPasswordValidationLacksConfirmPassword(TestCase):
    """Confirm passwrod lacks."""

    def setUp(self):
        """setup."""
        self.form = CurrentPasswordTestForm(MultiDict({
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


class CurrentPasswordValidationLacksNewPassword(TestCase):
    """New passwrod lacks."""

    def setUp(self):
        """setup."""
        self.form = CurrentPasswordTestForm(MultiDict({
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


class CurrentPasswordValidationLacksCurrentPassword(TestCase):
    """New passwrod lacks."""

    def setUp(self):
        """setup."""
        self.form = CurrentPasswordTestForm(MultiDict({
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


class CurrentPasswordValidationCurrentPasswordNotMatch(TestCase):
    """New passwrod lacks."""

    def setUp(self):
        """setup."""
        self.form = CurrentPasswordTestForm(MultiDict({
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


def gen_conditional_validation_form(dynamic, non_dynamic_exp=True):
    """Generate validation test form."""
    exp = (lambda form, field: form.email.data) if dynamic else non_dynamic_exp

    class ConditionalValidationTestForm(Form):
        class ValidationMock(object):
            mock = MagicMock()

            def __call__(self, *args, **kwargs):
                self.mock(*args, **kwargs)

        mock = ValidationMock
        email = fld.StringField()
        target = fld.StringField(validators=[ValidateTrue(mock, exp)])

    return ConditionalValidationTestForm


class ConditionalStaticNotValidationTest(TestCase):
    """Test case that shouldn't validate the value."""

    def setUp(self):
        """Setup."""
        self.formcls = gen_conditional_validation_form(False, False)
        self.form = self.formcls(data={"target": "test"})
        self.form.validate()

    def test_validation(self):
        """The form shouldn't validate target field."""
        self.form.mock.mock.assert_not_called()


class ConditionalStaticValidationTest(TestCase):
    """Test case that should validate the value."""

    def setUp(self):
        """Setup."""
        self.formcls = gen_conditional_validation_form(False, True)
        self.form = self.formcls(data={
            "email": "test@example.com",
            "target": "test"
        })
        self.form.validate()

    def test_validation(self):
        """The form shouldn't validate target field."""
        self.form.mock.mock.assert_called_once_with(
            self.form, self.form.target
        )


class ConditionalDynamicNotValidationTest(TestCase):
    """Test case that shouldn't validate the value."""

    def setUp(self):
        """Setup."""
        self.formcls = gen_conditional_validation_form(True)
        self.form = self.formcls(data={"target": "test"})
        self.form.validate()

    def test_validation(self):
        """The form shouldn't validate target field."""
        self.form.mock.mock.assert_not_called()


class ConditionalDynamicValidationTest(TestCase):
    """Test case that should validate the value."""

    def setUp(self):
        """Setup."""
        self.formcls = gen_conditional_validation_form(True)
        self.form = self.formcls(data={
            "email": "test@example.com",
            "target": "test"
        })
        self.form.validate()

    def test_validation(self):
        """The form shouldn't validate target field."""
        self.form.mock.mock.assert_called_once_with(
            self.form, self.form.target
        )
