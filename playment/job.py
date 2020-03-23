from playment.data import Data
from playment.batch_handler import Batch


# todo: batchId to be used
class Job:
    def __init__(self, reference_id: str, tag: str, data: Data, _id: str = None,
                 priority_weight: int = 5, batch_id: str = None):
        self._id = _id
        self.reference_id = reference_id
        self.tag = tag
        self.data = data
        self.batch_id = batch_id
        self.priority_weight = priority_weight
