from start import StartActor
import redis as redis_connector
from ..manager.manager import manager
from PIL import Image


class RedisActor(StartActor):

    CHANNEL = 'tasks'
    SEPARATOR = '_'
    PATH_SEPARATOR = '=>'
    def __init__(self):
        self.connection = redis_connector.StrictRedis(host='localhost', port=6379, db=0)
        self.subscriber = self.connection.pubsub(ignore_subscribe_messages=True)
        self.path = ''
        StartActor.__init__(self)

    def get_path(self):
        return self.path.split(self.PATH_SEPARATOR)

    def handle(self, msg):
        print msg
        arguments, path = msg.split(self.SEPARATOR)
        arguments = self.connection.get(arguments)
        path = self.connection.get(path)
        if not path or not arguments:
            return
        self.path = path
        parsed_path = self.get_path()
        im = Image.open(arguments)

        manager.go_next(parsed_path[0], {'path': parsed_path,'args':im})

    def prepare_input(self):
        self.subscriber.subscribe(self.CHANNEL)
        for msg in self.subscriber.listen():
            self.handle(msg['data'])



