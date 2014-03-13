from django.shortcuts import render, redirect
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from socketio.sdjango import namespace
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from models import Project, Job
from django.core.urlresolvers import reverse, reverse_lazy
import logging
from django.shortcuts import render_to_response


@namespace('/chat')
class ChatNamespace(BaseNamespace):
    def initialize(self):
        print 'socketio session started'
        self.logger = logging.getLogger("socketio.chat")
        self.log("Socketio session started")

    def log(self, message):
        self.logger.info("[{0}] {1}".format(self.socket.sessid, message))

    def on_chat(self, msg):
        print 'received: %s' % msg
        self.emit('chat', 'you said: %s' % msg)


class Projects(ListView):
    model = Project

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        return render_to_response('collaboration/projects.html', {'projects': projects})


class CreateProject(CreateView):
    model = Project
    fields = ['name']
    template_name = 'collaboration/create_project.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        Project(name=name).save()
        return redirect(reverse('projects_list'))


class DetailProject(DetailView):
    model = Project

    def get(self, request, *args, **kwargs):
        name = kwargs.get('slug')
        project = Project.objects.get(name=name)
        project = {
            'name': project.name,
            # 'jobs': project.jobs.all()

        }
        return render_to_response('collaboration/detail_project.html', {'project': project})


class DeleteProject(DeleteView):
    model = Project

    def get(self, request, *args, **kwargs):
        name = kwargs.get('slug')
        project = Project.objects.get(name=name)
        return render_to_response('collaboration/delete_project.html', {'name': project.name})

    def post(self, request, *args, **kwargs):
        name = request.get('slug')
        Project.objects.get(name=name).delete()

        return redirect(reverse_lazy('projects_list'))


class CreateJob(CreateView):
    model = Job
    fields = ['name']
    template_name = 'collaboration/create_job.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        Project(name=name).save()
        return redirect(reverse('project_detail', kwargs={'slug': name}))


class DeleteJob(CreateView):
    model = Job


def socketio(request):
    '''main notification view'''
    socketio_manage(
        request.environ,
        {'/chat': ChatNamespace},
        request
    )


def test(request):
    return render(
        request,
        'collaboration/test.html'
    )
