#!/usr/bin/env python
# coding=utf-8

"""Controllers for legal notation."""

from django.conf import settings
from django.views.generic import TemplateView
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _lz

from hysoftware_data.legal import ActReader, copyright
from hysoftware_data.users import Users


class LegalView(TemplateView):
    """Legal view."""

    template_name = "legal.html"
    ng_app = "legal"
    description = _lz("Legal Statement")
    acts = ActReader()
    users = Users(settings.NAME)

    @cached_property
    def regulations(self):
        """Return countries where the required notation is recognized."""
        return self.acts

    @cached_property
    def users_info(self):
        """Return hysoft staff's information."""
        return self.users

    @cached_property
    def assets_info(self):
        """Retrn third party asset model."""
        return copyright
