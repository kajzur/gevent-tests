from ..abstract_actor import AbstractActor
from PIL import ImageFilter

class Blur(AbstractActor):
    def process(self, img):
        blurred = img.filter(ImageFilter.BLUR)
        return blurred