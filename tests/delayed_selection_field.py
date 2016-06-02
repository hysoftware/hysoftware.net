#!/usr/bin/env python
# coding=utf-8

"""Delayed selection field tests."""

from unittest import TestCase
from unittest.mock import MagicMock
from wtforms.form import Form

from app.common import DelayedSelectField


class NonDelayedEvaluationTest(TestCase):
    """Test case that the field evaluates choices right away."""

    def setUp(self):
        """setup."""
        self.data = [
            (("t{}").format(counter), ("test{}").format(counter))
            for counter in range(3)
        ]

        class TestForm(Form):
            field = DelayedSelectField(choices=self.data)

        self.form = TestForm()

    def test_iter_choices(self):
        """Iter choices returns the exactly-same value."""
        for index, result in enumerate(self.form.field.iter_choices()):
            self.assertSequenceEqual(result[:-1], self.data[index])


class DelayedEvaluationTest(TestCase):
    """Test case that the field evaluates choices with delayed."""

    def setUp(self):
        """setup."""
        self.data = MagicMock(return_value=[
            (("t{}").format(counter), ("test{}").format(counter))
            for counter in range(3)
        ])

        class TestForm(Form):
            field = DelayedSelectField(choices=self.data)

        self.form = TestForm()

    def test_iter_choices(self):
        """Iter choices returns the exactly-same value."""
        self.data.assert_not_called()
        for index, result in enumerate(self.form.field.iter_choices()):
            self.assertSequenceEqual(
                result[:-1], self.data.return_value[index]
            )
        self.data.assert_called_once_with()
