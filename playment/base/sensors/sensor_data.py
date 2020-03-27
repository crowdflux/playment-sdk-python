from playment.base.data import Data
from playment.base.sensors.sensor_fusion_data import SensorFusionData
from playment.base.sensors.sensor import Sensor
from playment.base.sensors.frame import Frame


class SensorData(Data):
    def __init__(self, sensor_fusion_data: SensorFusionData = SensorFusionData(), metadata=None):
        assert type(sensor_fusion_data) is SensorFusionData
        self.sensor_data = sensor_fusion_data
        self.metadata = metadata

    def add_sensor(self, sensor: Sensor):
        assert type(sensor) is Sensor
        self.sensor_data.add_sensor(sensor)

    def add_frame(self, frame: Frame):
        assert type(frame) is Frame
        self.sensor_data.add_frame(frame)

    def valid(self):
        pass
