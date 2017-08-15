import gevent
from actors.abstract_actor import AbstractActor
from actors.finish_actors import *
from actors.initial_actors import *
from actors.processing_actors import *
ABSTRACT_ACTORS = ['StartActor']

def inheritors(klass):
    subclasses = []
    work = klass
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                if child.__name__ not in ABSTRACT_ACTORS:
                    subclasses.append(child)
                work.append(child)
    return subclasses

def setup():
    all_actors = inheritors([AbstractActor, StartActor])
    all_actors_instances = [actor() for actor in all_actors]
    to_join = []
    for actor in all_actors_instances:
        actor.start()
        manager.add(actor)
        to_join.append(actor)

    print 'Created %r' % to_join

    gevent.joinall(to_join)


setup()