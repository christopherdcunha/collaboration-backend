from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from collaboration.models import Project, Job


class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        authorization = DjangoAuthorization()


class JobResource(ModelResource):
    class Meta:
        queryset = Job.objects.all()
        authorization = DjangoAuthorization()
