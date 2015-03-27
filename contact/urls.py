'''
Contact form URL routing
'''

from django.conf.urls import patterns, url
from .views import contact

# pylint: disable=invalid-name
urlpatterns = patterns(
    "",
    url(
        r"^$",
        contact,
        name='contact_view_without_hash'
    ),
    url(
        r"^(?P<developer_hash>[0-9,a-f]{40})$",
        contact,
        name='contact_view_with_hash'
    )
)
# pylint: enable=invalid-name
