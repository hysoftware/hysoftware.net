'''
URL router
'''

from django.conf.urls import patterns, url
from .views import index

# pylint: disable=invalid-name
urlpatterns = patterns(
    "",
    url(r"^$", index, name='index')
)
# pylint: enable=invalid-name
