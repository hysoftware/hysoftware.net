'''
Contact form URL routing
'''

from django.conf.urls import patterns, url
from .views import contact

# pylint: disable=invalid-name
urlpatterns = patterns(
    "",
    url(r"^$", contact, name='contact_view')
)
# pylint: enable=invalid-name
