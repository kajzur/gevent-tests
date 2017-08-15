from ..abstract_actor import AbstractActor
from PIL import ImageFilter

class Detail(AbstractActor):
    def process(self, img):
        detailed = img.filter(ImageFilter.DETAIL)
        return detailed