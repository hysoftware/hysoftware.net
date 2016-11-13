#!/usr/bin/env python
# coding=utf-8

"""Home module."""

from django.conf.urls import url

from .views import HomeView, CSSView

app_name = "home"

urlpatterns = (
    url(r'^$', HomeView.as_view(), name="index"),
    url(r"^css$", CSSView.as_view(), name="css")
)
