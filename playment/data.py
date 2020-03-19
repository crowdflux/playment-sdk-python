from playment.datatype_handler import SensorFusionData
from playment.datatype_handler import ImageData


class Data:
    def __init__(self, data: SensorFusionData or ImageData):
        if type(data) == SensorFusionData:
            self.sensor_data = data
        else:
            self.image_url = data.image_url
