from ..abstract_actor import AbstractActor

class FinishActor(AbstractActor):
    def process(self, message):
        print "huj"
        print message
