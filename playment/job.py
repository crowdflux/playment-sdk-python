from playment.data import Data
from playment.datatype_handler import SensorFusionData, ImageData
from playment.batch_handler import Batch
import json


def to_dict(obj):
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )


# todo: batchId to be used
class Job:
    def __init__(self, reference_id: str, tag: str, data: Data,
                 priority_weight: int = 5, batch: Batch = None):
        self.reference_id = reference_id
        self.tag = tag
        self.data = data
        self.batch_id = batch.batch_id if batch is not None else batch
        self.priority_weight = priority_weight

    def as_dict(self, job):
        return json.loads(
            json.dumps(job, default=lambda o: getattr(o, '__dict__', str(o)))
        )
