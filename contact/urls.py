'''
Contact form URL routing
'''

from django.conf.urls import patterns, url
from .views import (
    Contact,
    check_email_in_list,
    verify_address
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
        r"^/verify/(?P<mail_hash>[0-9,a-f]{40})",
        verify_address,
        name="verify_address"
    )
)
# pylint: enable=invalid-name
