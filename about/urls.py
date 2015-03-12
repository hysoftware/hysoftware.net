'''
URL router
'''

from django.conf.urls import patterns, url
from .views import about_view

# pylint: disable=invalid-name
urlpatterns = patterns(
    "",
    url(r"^$", about_view, name='about_view')
)
# pylint: enable=invalid-name
