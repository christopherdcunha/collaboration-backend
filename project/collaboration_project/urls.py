from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from collaboration.views import (
    Projects,
    DetailProject,
    CreateProject,
    DeleteProject,
    CreateJob,
    DeleteJob
)

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
    url(r'^projects/$',
        Projects.as_view(),
        name='projects_list'
    ),
    url(r'^project/create/$',
        CreateProject.as_view(),
        name='create_project'
    ),
    url(
        r'^project/detail/(?P<slug>[-\w]+)/$',
        DetailProject.as_view(),
        name='detail_project'
    ),
    url(r'^project/delete/(?P<slug>[-\w]+)/$',
        DeleteProject.as_view(),
        name='delete_project'
    ),
    url(
        r'^job/create/$',
        CreateJob.as_view(),
        name='create_job'
    ),
    url(
        r'^job/delete/$',
        DeleteJob.as_view(),
        name='delete_job'

    ),
    url(
        r'^socket\.io/',
        include('collaboration.urls')
    ),
    url(r'^api/', include('api.urls')),
)
urlpatterns += staticfiles_urlpatterns()
