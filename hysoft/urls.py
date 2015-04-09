'''
Main module URL definition
'''

from django.conf.urls import patterns, include, url
from django.contrib import admin

# Examples:
# url(r'^$', 'hysoft.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
# pylint: disable=invalid-name
urlpatterns = patterns(
    '',
    url(r"^", include("home.urls")),
    url(r"^about", include("about.urls")),
    url(r"^contact", include("contact.urls")),
    url(r'^manager/', include(admin.site.urls))
)
