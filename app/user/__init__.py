#!/usr/bin/env python
# coding=utf-8

"""User related module."""


from django.conf.urls import url
from ..common.utils import gen_uuid_pattern
from .views import AboutView, CSSView, MemberDialog, JSView


app_name = "user"

urlpatterns = (
    url(r"^about$", AboutView.as_view(), name="about"),
    url(r"^css$", CSSView.as_view(), name="css"),
    url(r"^js$", JSView.as_view(), name="js"),
    url(
        r"^staff/" + gen_uuid_pattern("info_id") + r"$",
        MemberDialog.as_view(), name="staff"
    )
)
