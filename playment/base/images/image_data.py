from playment.base.data import Data


class ImageData(Data):
    def __init__(self, image_url: str, metadata=None):
        self.image_url = image_url
        self.metadata = metadata

    def valid(self):
        pass
