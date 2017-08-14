import gevent
from gevent.queue import Queue
from gevent.local import local
from exceptions import NotImplementedError
from manager.manager import manager

class AbstractActor(gevent.Greenlet):

    def __init__(self):
        self.inbox = Queue()
        self.local_storage = local()
        gevent.Greenlet.__init__(self)

    def process(self, args):
        raise NotImplementedError()

    def receive(self, message):   
        arguments = message['args']
        path = message['path']
        current_step = path.pop()
        args = self.process(arguments)
        self.go_next(current_step, {
            'args': args,
            'path': path
        })

    def go_next(self, name, message):
        actor = manager.get_next_actor(name)
        actor.inbox.put(message)

    def _run(self):
        self.running = True

        while self.running:
            print 'waiting for msg on %r' %self
            message = self.inbox.get()
            print 'msg %r' %message
            self.receive(message)
