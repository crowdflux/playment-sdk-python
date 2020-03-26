from playment.base.data import Data


class ImageData(Data):
    def __init__(self, image_url: str, metadata=None):
        assert type(image_url) is str
        self.image_url = image_url
        self.metadata = metadata

    def valid(self):
        assert len(self.image_url.split("/")) > 3
        pass
