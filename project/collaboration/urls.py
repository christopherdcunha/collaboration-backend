from django.conf.urls import patterns, include, url

import socketio.sdjango
socketio.sdjango.autodiscover()

urlpatterns = patterns(
    "collaboration.views",
    url("", include(socketio.sdjango.urls)),
)
