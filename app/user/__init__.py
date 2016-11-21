#!/usr/bin/env python
# coding=utf-8

"""User related module."""


from django.conf.urls import url
from .views import AboutView, CSSView


app_name = "user"

urlpatterns = (
    url(r"^about$", AboutView.as_view(), name="about"),
    url(r"^css$", CSSView.as_view(), name="css")
)
