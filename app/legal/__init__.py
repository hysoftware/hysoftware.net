#!/usr/bin/env python
# coding=utf-8

"""Legal notaion module."""

from django.conf.urls import url
from .views import LegalView, CSSView, JSView

app_name = "legal"

urlpatterns = (
    url(r"^$", LegalView.as_view(), name="index"),
    url(r"^css$", CSSView.as_view(), name="css"),
    url(r"^js$", JSView.as_view(), name="js")
)
