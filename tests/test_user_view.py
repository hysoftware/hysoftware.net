#!/usr/bin/env python
# coding=utf-8

"""User view tests."""

import uuid
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase

from app.user.views import AboutView, CSSView, MemberDialog
from app.user.models import UserInfo
from .view_base import TemplateViewTestBase


class AboutPageTest(TemplateViewTestBase, TestCase):
    """About page test."""

    endpoint = "user:about"
    page_url = "/u/about"
    view_cls = AboutView
    template_name = "about.html"

    @patch("app.user.models.UserInfo.objects")
    def test_users_info_property(self, objects):
        """User Info property should return the queryset of user info."""
        self.assertIs(self.view_cls().users_info, objects)


class MemberPageTest(TemplateViewTestBase, TestCase):
    """Member page test."""

    endpoint = "user:staff"
    view_cls = MemberDialog
    template_name = "member_dialog.html"
    info_id = uuid.uuid4()
    page_url = ("/u/staff/{}").format(str(info_id))
    url_kwargs = {"info_id": str(info_id)}

    def setUp(self):
        """SetUp."""
        self.user = get_user_model().objects.create_user(
            username="test", password="test"
        )
        self.info = UserInfo.objects.create(
            id=self.info_id, user=self.user, github="octocat"
        )
        self.page_url = ("/u/staff/{}").format(str(self.info.id))

    def tearDown(self):
        """Teardown."""
        get_user_model().objects.all().delete()
        UserInfo.objects.all().delete()


class CSSPagetest(TemplateViewTestBase, TestCase):
    """CSS view test."""

    endpoint = "user:css"
    page_url = "/u/css"
    view_cls = CSSView
    template_name = "user.css"
    content_type = "text/css"
