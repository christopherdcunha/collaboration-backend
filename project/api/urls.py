from api import resources

from django.conf.urls import include, patterns
from tastypie.api import Api

api_v1 = Api(api_name='v1')
api_v1.register(resources.ProjectResource())
api_v1.register(resources.JobResource())

urlpatterns = patterns(
    '',
    (r'^', include(api_v1.urls)),
)
