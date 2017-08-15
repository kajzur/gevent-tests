import gevent
from gevent.queue import Queue
from gevent.local import local
from exceptions import NotImplementedError
from manager.manager import manager

class AbstractActor(gevent.Greenlet):

    def __init__(self):
        self.inbox = Queue()
        self.local_storage = local()
        print 'Creating %r ...' % self
        gevent.Greenlet.__init__(self)

    def process(self, args):
        raise NotImplementedError()

    def receive(self, message):   
        arguments = message['args']
        path = message['path']
        if len(path) > 1:
            next_step = path[-1]
            path.pop()
        else:
            next_step = None

        print 'Processing in %r, next will be %r' % (self, next_step)
        args = self.process(arguments)
        if args:
            manager.go_next(next_step, {
                'args': args,
                'path': path
            })

    def _run(self):
        self.running = True
        print 'Waiting in %r' % self
        while self.running:
            message = self.inbox.get()
            self.receive(message)
