#!/usr/bin/env python
# coding=utf-8

"""Controllers for legal notation."""

from django.urls import reverse
from django.views.generic import TemplateView
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _lz, ugettext as _


class LegalView(TemplateView):
    """Legal view."""

    template_name = "legal.html"
    ng_app = "legal"
    description = _lz("Legal Statement")

    @cached_property
    def country(self):
        """Return countries where the required notation is recognized."""
        from .models import RecognizedCountry
        return RecognizedCountry.objects

    @cached_property
    def users_info(self):
        """Return hysoft staff's information."""
        from ..user.models import UserInfo
        return UserInfo.objects

    @cached_property
    def assets_info(self):
        """Retrn third party asset model."""
        return [
            {
              "name": _("Homepage Title Background"),
              "page": reverse("home:index"),
              "license": "CC0",
              "source": "http://alana.io/downloads/apple-macbook-laptop/",
              "license_url": "http://alana.io/license/",
              "check_date": "2017-07-18"
            }, {
              "name": _("Legal Page Title Background"),
              "page": reverse("legal:index"),
              "license": "CC0",
              "source": "http://alana.io/downloads/book-3/",
              "license_url": "http://alana.io/license/",
              "check_date": "2017-07-18"
            }, {
              "name": _("About Page Title Background"),
              "page": reverse("user:about"),
              "license": "CC0",
              "source": "http://alana.io/downloads/menu-2",
              "license_url": "http://alana.io/license/",
              "check_date": "2017-07-18"
            }, {
              "name": _("Contact Page Title Background"),
              "page": reverse("user:contact"),
              "license": "CC0",
              "source": "http://alana.io/downloads/iphone/",
              "license_url": "http://alana.io/license/",
              "check_date": "2017-07-18"
            }
        ]
