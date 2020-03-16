from playment.datatype_handler import SensorFusionData, ImageData
from playment.batch_handler import Batch
import json


def to_dict(obj):
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )


class Job:
    def __init__(self, reference_id: str, tag: str, data: SensorFusionData or ImageData,
                 priority_weight: int = 5, batch: Batch = None):
        self.reference_id = reference_id
        self.tag = tag
        self.data = to_dict(data) if type(data) == ImageData else {"sensor_data": to_dict(data)}
        self.batch_id = batch.batch_id if batch is not None else batch
        self.priority_weight = priority_weight
