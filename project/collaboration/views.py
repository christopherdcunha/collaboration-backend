from django.shortcuts import render
from socketio import socketio_manage
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
