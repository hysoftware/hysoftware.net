#!/usr/bin/env python
# coding=utf-8

"""Legal notaion module."""

from django.conf.urls import url
from .views import LegalView

app_name = "legal"

urlpatterns = (
    url(r"^$", LegalView.as_view(), name="index"),
)
