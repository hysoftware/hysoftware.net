#!/usr/bin/env python
# coding=utf-8

"""User related module."""


from django.conf.urls import url
from .views import AboutView


app_name = "user"

urlpatterns = (
    url(r"^about$", AboutView.as_view(), name="about"),
)
