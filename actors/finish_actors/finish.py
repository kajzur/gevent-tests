from ..abstract_actor import AbstractActor
import string, random

class FinishActor(AbstractActor):

    def random_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def process(self, img):
        print 'Saving in format %r .... ' % 'jpg'
        filename = '/home/mmazurek/' + self.random_generator() + '.jpg'
        img.save(filename, img.format)
        print 'Saved in %r' % filename

