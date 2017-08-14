#from ..abstract_actor import AbstractActor
from exceptions import AssertionError
import random
import gevent

class Manager():

    def __init__(self):
        self.dictionary = dict()

    def add(self, obj):
 #       if not isinstance(obj, AbstractActor):
  #          raise AssertionError('Object must be as instance of AbstractActor!')
        class_name = obj.__class__.__name__
        if self.dictionary.has_key(class_name):
            self.dictionary[class_name].append(obj)
        else:
            self.dictionary[class_name] = [obj]

    def get_next_actor(self, name):
        if not self.dictionary.has_key(name):
            print 'Actor %s not found!' % name
            name = 'FinishActor'
        return random.choice(self.dictionary[name])

    def go_next(self, next_path, args):
        actor_instance = self.get_next_actor(next_path)
        print 'Putting into  %r, is run:' % actor_instance
        actor_instance.inbox.put(args)
        gevent.sleep(0)

manager = Manager()

