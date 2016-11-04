#!/usr/bin/env python
# coding=utf-8

"""View test base."""

from django.core.urlresolvers import reverse, resolve
from django.test import RequestFactory
from django.views.generic import TemplateView


class TemplateViewTestBase(object):
    """View test base."""

    method = "get"

    def __init__(self, *args, **kwargs):
        """Setup."""
        self.request = getattr(RequestFactory(), self.method)(self.page_url)

        if not getattr(self, "view", None):
            self.view = self.view_cls.as_view()
        super(TemplateViewTestBase, self).__init__(*args, **kwargs)

    def test_class(self):
        """The view class should be a subclass of TemplateView."""
        self.assertTrue(issubclass(self.view_cls, TemplateView))

    def test_url(self):
        """The URL should be found in the app."""
        self.assertEqual(reverse(self.endpoint), self.page_url)

    def test_assignment(self):
        """The view should be assigned to URL."""
        self.assertEqual(
            resolve(self.page_url).func.__name__, self.view.__name__
        )

    def test_template(self):
        """The TemplateView should have proper template name."""
        self.assertEqual(self.view_cls.template_name, self.template_name)

    def test_content_type(self):
        """The content type should be expected."""
        self.assertEqual(
            self.view_cls.content_type,
            getattr(self, "content_type", None)
        )
