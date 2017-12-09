#!/usr/bin/env python
# coding=utf-8

"""Test home view."""

from unittest.mock import patch
from django.test import TestCase
# from django.urls import reverse

from app.home.views import HomeView, SSLValidationView

from .view_base import TemplateViewTestBase


class HomeViewRenderingTest(TemplateViewTestBase, TestCase):
    """Home View Rendering Test."""

    template_name = "home.html"
    endpoint = "home:index"
    page_url = "/"
    view_cls = HomeView

    @patch("app.home.models.Pitch.objects")
    @patch("app.home.views.get_language_from_request", return_value="en-us")
    def test_pitch_property(self, get_lang, pitch_objs):
        """
        The pitch should call Pitch.objects.choice in proper language.

        In addition to this, the return value should be proper.
        """
        view_obj = self.view_cls()
        view_obj.request = self.request
        self.assertEqual(
            view_obj.pitch,
            getattr(
                pitch_objs.choice.return_value,
                "text_%s" % get_lang.return_value.replace("-", "_")
            )
        )
        get_lang.assert_called_once_with(self.request)
        pitch_objs.choice.assert_called_once_with()

    @patch("app.home.models.Pitch.objects")
    @patch("app.home.views.get_language_from_request", return_value="en-us")
    def test_pitch_property_no_language(self, get_lang, pitch_objs):
        """
        It should show the defualt text if the translation is empty.

        In addition to this, the return value should be proper.
        """
        view_obj = self.view_cls()
        view_obj.request = self.request
        pitch_objs.choice.return_value.text_en_us = None
        self.assertEqual(view_obj.pitch, pitch_objs.choice.return_value.text)
        get_lang.assert_called_once_with(self.request)
        pitch_objs.choice.assert_called_once_with()

    @patch("app.home.models.Pitch.objects")
    @patch("app.home.views.get_language_from_request", return_value="en-us")
    def test_pitch_property_exception(self, get_lang, pitch_objs):
        """
        It should show the defualt text if the translation is unavailable.

        In addition to this, the return value should be proper.
        """
        view_obj = self.view_cls()
        view_obj.request = self.request
        del pitch_objs.choice.return_value.text_en_us
        self.assertEqual(view_obj.pitch, pitch_objs.choice.return_value.text)
        get_lang.assert_called_once_with(self.request)
        pitch_objs.choice.assert_called_once_with()

    def test_user_property(self):
        """Should return a queryset of user info object."""
        from app.user.models import UserInfo
        self.assertIs(self.view_cls().users_info, UserInfo.objects)


class SSLValidationTextTest(TemplateViewTestBase, TestCase):
    """SSL Validation text test."""

    template_name = "A19129EBDFBB9D747449765BAEB1C234.txt"
    content_type = "text/plain"
    view_cls = SSLValidationView
    endpoint = "home:ssl"
    page_url = "/A19129EBDFBB9D747449765BAEB1C234.txt"
