'''
Main module URL definition
'''

# pylint: disable=invalid-name

from django.conf.urls import patterns, include, url
from django.contrib import admin

# Examples:
# url(r'^$', 'hysoft.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)
