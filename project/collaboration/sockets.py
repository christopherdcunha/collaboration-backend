import json
import logging

from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from socketio.sdjango import namespace

import gevent
from django.contrib.contenttypes.models import ContentType
from collaboration.models import Project, Job
from tastypie.serializers import Serializer
from api.resources import ProjectResource, JobResource
from simple_audit.models import Audit

serializer = Serializer()


def get_or_none(model, id):
    try:
        return model.objects.get(id=id)
    except model.DoesNotExist:
        return None


def get_serialized_data(model, resource, id):
    print (model, resource, id)
    obj = get_or_none(model, id)

    if obj is None:
        return None

    return resource.full_dehydrate(
        resource.build_bundle(
            obj=obj
        ),
        for_list=True
    )


@namespace('/project')
class ProjectNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):
    def initialize(self):
        self.logger = logging.getLogger("socketio.chat")
        self.log("Socketio session started")
        self.spawn(self.job_send_latest)
        self.session['last_audit_date'] = Audit.objects.latest('date').date

    def log(self, message):
        self.logger.info("[{0}] {1}".format(self.socket.sessid, message))

    def on_test(self, msg):
        print 'received: %s' % msg
        self.emit('test', {
            'project': {
                2: {'name': 'I am a project'}
            },
            'job': {
                5: {'name': 'I am a job'}
            }
        })

    def on_join(self, room):
        self.room = room
        self.join(room)
        return True

    def job_send_latest(self):
        project_resource = ProjectResource()
        job_resource = JobResource()
        while True:
            project_audits = Audit.objects.filter(
                date__gt=self.session['last_audit_date'],
                content_type=ContentType.objects.get_for_model(Project)
            )
            job_audits = Audit.objects.filter(
                date__gt=self.session['last_audit_date'],
                content_type=ContentType.objects.get_for_model(Job)
            )
            self.session['last_audit_date'] = Audit.objects.latest('date').date
            if project_audits or job_audits:
                bundles = {
                    'project': dict(
                        (
                            audit.object_id,
                            get_serialized_data(
                                Project,
                                project_resource,
                                audit.object_id
                            )
                        ) for audit in project_audits
                    ),
                    'job': dict(
                        (
                            audit.object_id,
                            get_serialized_data(
                                Job,
                                job_resource,
                                audit.object_id
                            )
                        ) for audit in job_audits
                    )
                }
                self.emit(
                    'project',
                    json.loads(
                        project_resource.serialize(
                            None,
                            bundles,
                            "application/json"
                        )
                    )
                )
            gevent.sleep(0.2)
