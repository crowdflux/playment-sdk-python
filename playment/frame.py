from playment.sensors.sensor import Sensor
from typing import List


class Frame:
    def __init__(self, frame_id: str = None, sensors: List[Sensor] = []):
        self.frame_id = frame_id
        self.sensors = sensors

    def add_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)
