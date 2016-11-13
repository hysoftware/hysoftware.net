#!/usr/bin/env python
# coding=utf-8

"""Commonly used package."""

from django.conf.urls import url
from .views import JSView, CSSView, ImageView


app_name = "common"

urlpatterns = (
    url(r'^js$', JSView.as_view(), name="js"),
    url(r'^css$', CSSView.as_view(), name="css"),
    url(r'^assets/(?P<filename>.+)$', ImageView.as_view(), name="assets")
)
