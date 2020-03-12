from playment.data import Data
from playment.batch_handler import Batch


class Job:
    def __init__(self, reference_id: str, tag: str, data: Data,
                 priority_weight: int = 5, batch: Batch = None):
        self.reference_id = reference_id
        self.tag = tag
        self.data = data
        self.batch_id = batch.batch_id if batch is not None else batch
        self.priority_weight = priority_weight
