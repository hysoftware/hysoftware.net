#!/usr/bin/env python
# coding=utf-8

"""User tasks."""

from unittest.mock import patch, call
from django.conf import settings
from django.test import TestCase

from app.user.tasks import fetch_github_profile

from hysoftware_data.users.users import User, Users


class GithubProfileUpdateTest(TestCase):
    """Github Profile Update test."""

    def setUp(self):
        """Setup."""
        super(GithubProfileUpdateTest, self).setUp()
        self.users = Users(settings.NAME)
        self.task = fetch_github_profile

    def test_task(self):
        """Should update the data."""
        with patch.object(User, "get_github_profile") as fetch_mock:
            self.task()
        self.assertEqual(
            len([
                item for item in fetch_mock.call_args_list
                if item == call(disable_cache=True)
            ]),
            len(self.users)
        )


class GithubProfileUpdateIndividualTest(TestCase):
    """Github Profile Update by individual test."""

    def setUp(self):
        """Setup."""
        super(GithubProfileUpdateIndividualTest, self).setUp()
        self.user = Users(settings.NAME)
        for user in self.user:
            for url in user.urls:
                if url["type"] == "github":
                    self.user = user
                    break
        self.task = fetch_github_profile

    def test_task(self):
        """Should update the data."""
        with patch.object(User, "get_github_profile") as fetch_mock:
            self.task(self.user.id)
        self.assertEqual(
            len([
                item for item in fetch_mock.call_args_list
                if item == call(disable_cache=True)
            ]), 1
        )
