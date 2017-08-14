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
    [manager.add(actor()) for actor in all_actors]
    to_join = []
    for actor in all_actors:
        instance_of_actor = actor()
        instance_of_actor.start()
        to_join.append(instance_of_actor)

    gevent.joinall(to_join)
 

setup()