#!/usr/bin/env python
# coding=utf-8

"""Home module."""

from django.conf.urls import url

from .views import HomeView, SSLValidationView

app_name = "home"

urlpatterns = (
    url(r'^$', HomeView.as_view(), name="index"),
    url(
        r"^A19129EBDFBB9D747449765BAEB1C234.txt$",
        SSLValidationView.as_view(), name="ssl"
    )
)
