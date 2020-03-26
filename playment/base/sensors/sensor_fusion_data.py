from playment.base.sensors.frame import Frame
from playment.base.sensors.sensor import Sensor
from typing import List


class SensorFusionData:
    def __init__(self, frames: List[Frame] = [], sensor: List[Sensor] = []):
        assert type(frames) is List[Frame]
        assert type(sensor) is List[Sensor]
        self.frames = frames
        self.sensor_meta = sensor

    def add_sensor(self, sensor: Sensor):
        assert type(sensor) is Sensor
        self.sensor_meta.append(sensor)

    def add_frame(self, frame: Frame):
        assert type(frame) is Frame
        self.frames.append(frame)
