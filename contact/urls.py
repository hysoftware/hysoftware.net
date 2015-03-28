'''
Contact form URL routing
'''

from django.conf.urls import patterns, url
from .views import contact, check_email_in_list

# pylint: disable=invalid-name
urlpatterns = patterns(
    "",
    url(r"^$", contact, name='contact_view'),
    url(r"^/(?P<dev_hash>[0-9,a-f]{40})$", contact, name='contact_view'),
    url(
        r"^/check/(?P<dev_hash>[0-9,a-f]{40})",
        check_email_in_list,
        name="check_email_in_list"
    )
)
# pylint: enable=invalid-name
