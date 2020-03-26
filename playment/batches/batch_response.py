from collections import namedtuple
from playment.utilities import Decodable


class BatchResponse(Decodable):
    def __init__(self, batch_id: str = None):
        assert type(batch_id) is str
        self.batch_id = batch_id

    def json_object_hook(self, d):
        return namedtuple('BatchResponse', d.keys())(*d.values())
