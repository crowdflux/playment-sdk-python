from collections import namedtuple


class BatchResponse:
    def __init__(self, batch_id: str = None):
        self.batch_id = batch_id

    def _json_object_hook(self, d):
        return namedtuple('BatchResponse', d.keys())(*d.values())
