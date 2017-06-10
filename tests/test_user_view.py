#!/usr/bin/env python
# coding=utf-8

"""User view tests."""

import uuid
import json
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory

from app.user.views import (
    AboutView, CSSView, MemberDialog, JSView, ContactView
)
from app.user.models import UserInfo, Inbox
from .view_base import TemplateViewTestBase


class AboutPageTest(TemplateViewTestBase, TestCase):
    """About page test."""

    endpoint = "user:about"
    page_url = "/u/about"
    view_cls = AboutView
    template_name = "about.html"

    def setUp(self):
        """Setup."""
        super(AboutPageTest, self).setUp()
        self.user = get_user_model().objects.create_user(
            username="Test Example", password="test"
        )
        self.info = UserInfo.objects.create(user=self.user, github="test")

    @patch("app.user.models.UserInfo.objects")
    def test_users_info_property(self, objects):
        """User Info property should return the queryset of user info."""
        self.assertIs(self.view_cls().users_info, objects)

    def test_view_description(self):
        """The description should be 'About me'."""
        self.assertEqual(self.view_cls().description, "About me")


class AboutPageMultipleUserInfoTest(TemplateViewTestBase, TestCase):
    """Multiple user information test."""

    endpoint = "user:about"
    page_url = "/u/about"
    view_cls = AboutView
    template_name = "about.html"

    def setUp(self):
        """Setup."""
        super(AboutPageMultipleUserInfoTest, self).setUp()
        self.users = [
            get_user_model().objects.create_user(
                username=("Test Example {}").format(counter),
                password="test"
            ) for counter in range(3)
        ]
        self.info = [
            UserInfo.objects.create(
                user=user, github=("test {}").format(user.username)
            )
            for user in self.users
        ]

    def test_view_description(self):
        """The description should be 'About us'."""
        self.assertEqual(self.view_cls().description, "About us")


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

    def test_user_info_property(self):
        """It should return user information."""
        view = self.view_cls()
        view.kwargs = {"info_id": str(self.info.id)}
        self.assertEqual(view.user_info, self.info)


class ContactPageTest(TemplateViewTestBase, TestCase):
    """Contact page test."""

    endpoint = "user:contact"
    template_name = "contact.html"
    info_id = uuid.uuid4()
    page_url = ("/u/contact/{}").format(info_id)
    url_kwargs = {"info_id": str(info_id)}
    view_cls = ContactView

    def setUp(self):
        """SetUp."""
        self.user = get_user_model().objects.create_user(
            username="test", password="test"
        )
        self.info = UserInfo.objects.create(
            id=self.info_id, user=self.user, github="octocat"
        )
        self.page_url = ("/u/contact/{}").format(str(self.info.id))

    def test_user_info_property(self):
        """It should return user information."""
        view = self.view_cls()
        view.kwargs = {"info_id": str(self.info.id)}
        self.assertEqual(view.user_info, self.info)

    def test_description(self):
        """The description should be 'Contact Form'."""
        self.assertEqual(self.view_cls().description, "Contact Form")

    @patch("app.user.forms.ContactForm")
    def test_form_get(self, form):
        """It should return view.info."""
        view = self.view_cls()
        view.request = self.request
        view.kwargs = self.url_kwargs
        self.assertIs(view.form, form.return_value)
        form.assert_called_once_with(info_id=str(self.info_id))

    @patch("app.user.forms.ContactForm")
    def test_form_post(self, form):
        """It should return view.info."""
        body = {
            "user": str(self.info_id),
            "company_name": "Test Corp",
            "primary_name": "Test Name",
            "email": "test@example.com",
            "message": "This is a test",
            "g-recaptcha-response": "PASSED"
        }
        view = self.view_cls()
        view.request = RequestFactory().post(
            self.page_url, json.dumps(body), content_type="applicatoin/json"
        )
        self.assertIs(view.form, form.return_value)
        form.assert_called_once_with(body)


class ContactPageWithoutInfoIDTest(TemplateViewTestBase, TestCase):
    """Contact page test."""

    endpoint = "user:contact"
    template_name = "contact.html"
    page_url = "/u/contact/"
    view_cls = ContactView

    @patch("app.user.models.UserInfo.objects")
    def test_users_info_property(self, objects):
        """It should return user information."""
        view = self.view_cls()
        self.assertEqual(view.users_info, objects)

    @patch("app.user.forms.ContactForm")
    def test_form_get(self, form):
        """It should return view.info."""
        view = self.view_cls()
        view.request = self.request
        view.kwargs = {"info_id": None}
        self.assertIs(view.form, form.return_value)
        form.assert_called_once_with()


class ContactPagePostMethodTest(TemplateViewTestBase, TestCase):
    """Contact page POST method test."""

    endpoint = "user:contact"
    template_name = "contact.html"
    info_id = uuid.uuid4()
    page_url = ("/u/contact/{}").format(info_id)
    view_cls = ContactView
    method = "post"
    url_kwargs = {"info_id": str(info_id)}

    def setUp(self):
        """SetUp."""
        self.body = {
            "user": str(self.info_id),
            "company_name": "Test Corp",
            "primary_name": "Test Name",
            "email": "test@example.com",
            "message": "This is a test",
            "g-recaptcha-response": "PASSED"
        }
        self.user = get_user_model().objects.create_user(
            username="test", password="test"
        )
        self.info = UserInfo.objects.create(
            id=self.info_id, user=self.user, github="octocat"
        )
        self.page_url = ("/u/contact/{}").format(str(self.info.id))
        self.request = RequestFactory().post(
            '/u/contact/', data=json.dumps(self.body),
            content_type="application/json"
        )

    def tearDown(self):
        """Teardown."""
        Inbox.objects.all().delete

    @patch("app.user.forms.zappa_async")
    @patch("app.user.forms.loader")
    def test_post_correct(self, loader, zappa_async):
        """Test post method with invalid payload."""
        result = self.view(self.request)
        inbox = Inbox.objects.get()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(inbox.user, self.info)

    @patch("app.user.forms.zappa_async")
    @patch("app.user.forms.loader")
    def test_post_invalid(self, loader, zappa_async):
        """Test post method with invalid payload."""
        self.body.pop("g-recaptcha-response", None)
        self.request = RequestFactory().post(
            '/u/contact/', data=json.dumps(self.body),
            content_type="application/json"
        )
        result = self.view(self.request)
        content = json.loads(result.content.decode("utf-8"))
        self.assertEqual(result.status_code, 417)
        self.assertDictEqual({"nobot": ["This field is required."]}, content)


class CSSPageTest(TemplateViewTestBase, TestCase):
    """CSS view test."""

    endpoint = "user:css"
    page_url = "/u/css"
    view_cls = CSSView
    template_name = "user.css"
    content_type = "text/css"


class JSPageTest(TemplateViewTestBase, TestCase):
    """JS view test."""

    endpoint = "user:js"
    page_url = "/u/js"
    view_cls = JSView
    template_name = "user.js"
    content_type = "application/javascript"
