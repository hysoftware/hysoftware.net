#!/usr/bin/env python
# coding=utf-8

"""Home db models."""

from random import choice
from django.db import models as db
from django.utils.translation import ugettext_lazy as _lz


class PitchManager(db.Manager):
    """Pitch queryset manager."""

    def choice(self):
        """Choice randomly from Pitch model."""
        try:
            return choice(self.get_queryset())
        except IndexError:
            return Pitch(text=_lz(
                "Oops. Hiro opened the website without what this website is."
            ))


class Pitch(db.Model):
    """The elevator pitch."""

    class Meta(object):
        """Metadata."""

        verbose_name = _lz("Pitch")
        verbose_name_plural = _lz("Pitches")

    text = db.TextField()
    objects = PitchManager()

    def __str__(self):
        """Represent the object."""
        return self.text
