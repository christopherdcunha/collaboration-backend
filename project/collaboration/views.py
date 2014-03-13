from django.shortcuts import render
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from socketio.sdjango import namespace
import logging
from collaboration.sockets import ProjectNamespace


def socketio(request):
    '''main notification view'''
    socketio_manage(
        request.environ,
        {'/project': ProjectNamespace},
        request
    )


def test(request):
    return render(
        request,
        'collaboration/test.html'
    )
