from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import socketio.sdjango
socketio.sdjango.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'collaboration_project.views.home', name='home'),
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'^test/',
        'collaboration.views.test',
        name='collaboration.test'
    ),
    url(r'^socket\.io/', include('collaboration.urls')),
)
urlpatterns += staticfiles_urlpatterns()
