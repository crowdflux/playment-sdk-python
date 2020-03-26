from playment.base.sensors.sensor import Sensor
from playment.base.sensors.frame import Frame
from playment.base.data import Data
from typing import List


class SensorFusionData:
    def __init__(self, frames: List[Frame] = [], sensor_meta: List[Sensor] = []):
        self.frames = frames
        self.sensor_meta = sensor_meta

    def add_sensor_meta(self, sensor_meta: Sensor):
        self.sensor_meta.append(sensor_meta)

    def add_frame(self, frame: Frame):
        self.frames.append(frame)


class ImageData(Data):
    def __init__(self, image_url: str):
        self.image_url = image_url

    def valid(self):
        pass
