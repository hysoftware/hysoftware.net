#!/usr/bin/env python
# coding=utf-8

"""User view tests."""

import json
from unittest.mock import patch

from django.conf import settings
from django.test import TestCase, RequestFactory
from hysoftware_data.users import Users

from app.user.views import (
    AboutView, CSSView, MemberDialog, JSView, ContactView
)
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
        self.user = Users(settings.NAME)[0]


class AboutPageMultipleUserInfoTest(TemplateViewTestBase, TestCase):
    """Multiple user information test."""

    endpoint = "user:about"
    page_url = "/u/about"
    view_cls = AboutView
    template_name = "about.html"

    def setUp(self):
        """Setup."""
        super(AboutPageMultipleUserInfoTest, self).setUp()
        self.users = Users(settings.NAME)

    def test_view_description(self):
        """The description should be 'About us'."""
        self.assertEqual(self.view_cls().description, "About us")


class MemberPageTest(TemplateViewTestBase, TestCase):
    """Member page test."""

    endpoint = "user:staff"
    view_cls = MemberDialog
    template_name = "member_dialog.html"
    user = Users(settings.NAME)[0]

    def setUp(self):
        """SetUp."""
        self.url_kwargs = {"info_id": self.user.id}
        self.page_url = ("/u/staff/{}").format(self.url_kwargs["info_id"])

    def test_user_info_property(self):
        """It should return user information."""
        view = self.view_cls()
        view.kwargs = {"info_id": str(self.url_kwargs["info_id"])}
        self.assertEqual(view.user_info, self.user)


class ContactPageTest(TemplateViewTestBase, TestCase):
    """Contact page test."""

    endpoint = "user:contact"
    template_name = "contact.html"
    view_cls = ContactView

    def setUp(self):
        """SetUp."""
        self.user = Users(settings.NAME)[0]
        self.url_kwargs = {
            "info_id": self.user.id
        }
        self.page_url = ("/u/contact/{}").format(
            str(self.url_kwargs["info_id"])
        )

    def test_user_info_property(self):
        """It should return user information."""
        view = self.view_cls()
        view.kwargs = self.url_kwargs
        self.assertEqual(view.user_info, self.user)

    def test_description(self):
        """The description should be 'Contact Form'."""
        self.assertEqual(self.view_cls().description, "Contact Form")

    @patch("app.user.forms.ContactForm")
    def test_method(self, form):
        """It should return view.info."""
        super(ContactPageTest, self).test_method()
        form.assert_called_once_with(info_id=str(self.url_kwargs["info_id"]))

    @patch("app.user.forms.ContactForm")
    def test_form_post(self, form):
        """It should return view.info."""
        body = {
            "user": str(self.url_kwargs["info_id"]),
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

    @patch("app.user.forms.ContactForm")
    def test_form_get(self, form):
        """It should return view.info."""
        view = self.view_cls()
        view.request = self.make_request()
        view.kwargs = {"info_id": None}
        self.assertIs(view.form, form.return_value)
        form.assert_called_once_with()


class ContactPagePostMethodTest(TemplateViewTestBase, TestCase):
    """Contact page POST method test."""

    endpoint = "user:contact"
    template_name = "contact.html"
    view_cls = ContactView
    method = "post"

    def setUp(self):
        """SetUp."""
        self.user = Users(settings.NAME)[0]
        self.url_kwargs = {"info_id": str(self.user.id)}
        self.page_url = ("/u/contact/{}").format(self.url_kwargs["info_id"])
        self.body = {
            "user": str(self.user.id),
            "company_name": "Test Corp",
            "primary_name": "Test Name",
            "email": "test@example.com",
            "message": "This is a test",
            "g-recaptcha-response": "PASSED"
        }
        self.set_client_kwargs(
            data=json.dumps(self.body),
            content_type="application/json"
        )

    @patch("app.user.forms.ctask")
    @patch("app.user.forms.loader")
    def test_method(self, loader, ctask):
        """Test method."""
        resp = super(ContactPagePostMethodTest, self).test_method()
        return resp


class ContactPagePostMethodInvalidPayloadTest(ContactPagePostMethodTest):
    """Contact page POST method test with invalid payload."""

    status_code = 417

    def setUp(self):
        """Setup."""
        super(ContactPagePostMethodInvalidPayloadTest, self).setUp()
        self.body.pop("g-recaptcha-response", None)
        self.set_client_kwargs(
            data=json.dumps(self.body),
            content_type="application/json"
        )

    def test_method(self):
        """Test post method with invalid payload."""
        resp = super(
            ContactPagePostMethodInvalidPayloadTest, self
        ).test_method()
        content = json.loads(resp.content.decode("utf-8"))
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
