#!/usr/bin/env python
# coding=utf-8

"""Test home view."""

from unittest.mock import patch
from django.test import TestCase

from app.common.models import ThirdPartyAssets
from app.home.views import HomeView, CSSView, HomeTitleImageView

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
        """"A queryset of user info object should be returned."""
        from app.user.models import UserInfo
        self.assertIs(self.view_cls().users_info, UserInfo.objects)


class HomeCSSViewRenderingTest(TemplateViewTestBase, TestCase):
    """Home stylesheet view rendering test."""

    template_name = "home.css"
    content_type = "text/css"
    view_cls = CSSView
    endpoint = "home:css"
    page_url = "/css"


class HomeTitleImageRenderingTest(TestCase):
    """Home title image view tests."""

    def setUp(self):
        """Setup."""
        from django.test import RequestFactory
        self.request = RequestFactory().get("/title")
        self.view = HomeTitleImageView.as_view()

    @patch("app.home.views.get_object_or_404")
    def test_image_fetch(self, objects):
        """The image should be read."""
        objects.return_value.image.read.return_value = "Test"
        result = self.view(self.request)
        objects.assert_called_once_with(ThirdPartyAssets, filename="home")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result["Content-Type"], "image/jpeg"
        )
        self.assertEqual(
            result.content.decode("utf-8"),
            objects.return_value.image.read.return_value
        )
