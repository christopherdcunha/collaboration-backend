from django.shortcuts import render
from socketio.namespace import BaseNamespace
from socketio import socketio_manage


class ChatNamespace(BaseNamespace):
    def on_chat(self, msg):
        self.emit('chat', msg)


def socketio(request):
    '''main notification view'''
    socketio_manage(
        request.environ,
        {'/chat': ChatNamespace},
        request
    )
