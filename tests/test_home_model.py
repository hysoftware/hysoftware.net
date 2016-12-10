#!/usr/bin/env python
# coding=utf-8

"""Test Home Model."""

from random import choice
from unittest.mock import patch
from django.test import TestCase
from app.home.models import Pitch


class PitchRepresentationTest(TestCase):
    """Pitch should represent itself."""

    def setUp(self):
        """Setup."""
        self.obj = Pitch(text="Hello")

    def test_represent(self):
        """Should show proper value."""
        self.assertEqual(str(self.obj), self.obj.text)


class PitchRandomChoiceTest(TestCase):
    """Pitch random choice funcitonality test."""

    def setUp(self):
        """Setup."""
        for counter in range(3):
            Pitch.objects.create(text=("Test {}").format(counter))

    @patch("app.home.models.choice", side_effect=choice)
    @patch("app.home.models.PitchManager.get_queryset", autospec=True)
    def test_choice(self, get_queryset, choice):
        """The choice method should be called."""
        def capture_queryset(obj):
            self.queryset_value = super(type(obj), obj).get_queryset()
            return self.queryset_value
        get_queryset.side_effect = capture_queryset
        Pitch.objects.choice()
        choice.assert_called_once_with(self.queryset_value)

    @patch("app.home.models.choice", side_effect=choice)
    def test_choice_return_value(self, choice):
        """The choice method should returns the proper value."""
        data = Pitch.objects.choice()
        self.assertIn(data, Pitch.objects.all())


class PitchWarningTest(TestCase):
    """If pitch wasn't found, dummy pitch should be returned."""

    @patch("app.home.models.choice", side_effect=choice)
    def test_choice(self, choice):
        """The dummy text should be returned."""
        data = Pitch.objects.choice()
        self.assertEqual(
            data.text,
            "Oops. Hiro opened the website without what this website is."
        )
