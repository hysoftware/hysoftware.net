#!/usr/bin/env python
# coding=utf-8

"""Legal model test cases."""

from django.test import TestCase

from app.legal.models import RecognizedCountry


class RecognizedCountryRepresentationTest(TestCase):
    """Recognized Country representation tests."""

    def setUp(self):
        """Setup."""
        self.ct = RecognizedCountry.objects.create(country="US")

    def test_represetation(self):
        """The represented text should be proper."""
        self.assertEqual(str(self.ct), self.ct.country.name)
