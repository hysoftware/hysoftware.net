'''
URL router
'''

from django.conf.urls import patterns, url
from .views import index, home

# pylint: disable=invalid-name
urlpatterns = patterns(
    "",
    url(r"^$", index, name='index'),
    url(r"^home", home, name='home'),
)
# pylint: enable=invalid-name
