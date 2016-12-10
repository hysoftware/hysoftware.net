#!/usr/bin/env python
# coding=utf-8

"""Common Database model."""

from django.utils.translation import ugettext_lazy as _lz
from django.db import models as db


class ThirdPartyAssets(db.Model):
    """
    Third party asset models.

    This model includes pictures from third party that is licensed with
    open-source, copyleft, or proprietary. For third party libs that this
    app depends, check requirements.txt, package.json, and bower.json.
    """

    class Meta(object):
        """Metadata."""

        verbose_name = _lz("Third Party Asset")
        verbose_name_plural = _lz("Third Party Assets")

    filename = db.CharField(max_length=40, primary_key=True)
    # 2097152 = 2MB
    image = db.ImageField(max_length=2097152)
    source = db.URLField(max_length=500)
    license = db.CharField(max_length=10)
    license_url = db.URLField()
    check_date = db.DateField(auto_now_add=True)
