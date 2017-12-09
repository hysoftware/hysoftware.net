#!/usr/bin/env python
# coding=utf-8

"""Database model for legal notation."""

from django.db import models as db
from django.utils.translation import ugettext_lazy as _lz
from django_countries.fields import CountryField


class RecognizedCountry(db.Model):
    """Country list that is recognized."""

    class Meta(object):
        """Metadata."""

        verbose_name_plural = _lz("Recognized Countries")

    country = CountryField()

    def __str__(self):
        """Represent the model."""
        return str(self.country.name)


class Act(db.Model):
    """Act list."""

    country = db.ForeignKey(
        RecognizedCountry, null=True, blank=True, on_delete=db.CASCADE
    )
    name = db.CharField(max_length=400)
    description = db.TextField()


class NotationTable(db.Model):
    """Notation table list."""

    act = db.ForeignKey(Act, on_delete=db.CASCADE)
    name = db.CharField(max_length=200)
    text = db.TextField()
