'''
Contact form URL routing
'''

from django.conf.urls import patterns, url
from .views import (
    Contact,
    check_email_in_list,
    AddressVerification
)

# pylint: disable=invalid-name
urlpatterns = patterns(
    "",
    url(r"^$", Contact.as_view(), name='contact_view'),
    url(
        r"^/(?P<dev_hash>[0-9,a-f]{40})$",
        Contact.as_view(),
        name='contact_view'
    ),
    url(
        r"^/check/(?P<dev_hash>[0-9,a-f]{40})",
        check_email_in_list,
        name="check_email_in_list"
    ),
    url(
        r"^/verify/(?P<token_hash>[0-9,a-f]{40})",
        AddressVerification.as_view(),
        name="verify_address"
    )
)
# pylint: enable=invalid-name
