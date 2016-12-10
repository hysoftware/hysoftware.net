#!/usr/bin/env python
# coding=utf-8

"""User model tests."""

from django.test import TestCase
from django.contrib.auth import get_user_model

from app.user.models import UserInfo, CodingLanguage


class UserInfoRepresentationTest(TestCase):
    """User info representation test."""

    def setUp(self):
        """Setup."""
        self.user = get_user_model().objects.create_user(
            username="test",
            first_name="Test",
            last_name="Example"
        )
        self.user_info = UserInfo.objects.create(
            user=self.user,
            title="Test title"
        )

    def test_representation(self):
        """The represented text should be proper."""
        self.assertEqual(
            str(self.user_info), ("{} {} ({})").format(
                self.user.first_name, self.user.last_name,
                self.user_info.title
            )
        )


class CodingLanguageRepresentationTest(TestCase):
    """Coding language representation test."""

    def setUp(self):
        """Setup."""
        self.lang = CodingLanguage.objects.create(name="test")

    def test_representation(self):
        """The represented text should be proper."""
        self.assertEqual(str(self.lang), self.lang.name)
