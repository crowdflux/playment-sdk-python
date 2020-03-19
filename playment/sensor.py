from playment.sensor_pose import SensorPose


class Sensor:
    def __init__(self, data_url: str = None, sensor_id: str = None):
        self.data_url = data_url
        self.sensor_id = sensor_id

    def add_sensor_pose(self, sensor_pose: SensorPose):
        self.sensor_pose = sensor_pose
