from playment.base.data import Data
from playment.datatype_handler import SensorFusionData


class SensorData(Data):
    def __init__(self, sensor_fusion_data: SensorFusionData = SensorFusionData(), metadata=None):
        assert type(sensor_fusion_data) is SensorFusionData
        self.sensor_data = sensor_fusion_data
        self.metadata = metadata

    def add_sensor_fusion_data(self, sensor_fusion_data: SensorFusionData):
        assert type(sensor_fusion_data) is SensorFusionData
        self.sensor_data = sensor_fusion_data

    def valid(self):
        pass
