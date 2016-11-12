#!/usr/bin/env python
# coding=utf-8

"""Home module."""

from django.conf.urls import url

from .views import HomeView, CSSView, HomeTitleImageView

app_name = "home"

urlpatterns = (
    url(r'^$', HomeView.as_view(), name="index"),
    url(r"^css$", CSSView.as_view(), name="css"),
    url(r'^title$', HomeTitleImageView.as_view(), name="title_image")
)
