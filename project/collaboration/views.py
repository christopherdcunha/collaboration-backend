from django.shortcuts import render
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from socketio.sdjango import namespace
import logging


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
