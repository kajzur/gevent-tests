from ..abstract_actor import AbstractActor
import gevent

class StartActor(gevent.Greenlet):

    def __init__(self):
        gevent.Greenlet.__init__(self)
        # self.prepare_input()

    def get_path(self):
        """
        Define in your subclass.
        """
        raise NotImplementedError()

    def prepare_input(self):
        """
        Define in your subclass.
        """
        raise NotImplementedError()

    def _run(self):
        self.prepare_input()

