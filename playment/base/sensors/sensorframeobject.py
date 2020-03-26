from playment.base.sensors.sensor_pose import SensorPose


class SensorFrameObject:
    def __init__(self, data_url: str = None, sensor_id: str = None, sensor_pose: SensorPose = None):
        assert type(data_url) is str
        assert len(data_url.split("/")) > 3
        assert type(sensor_id) is str
        assert type(sensor_pose) is SensorPose
        self.data_url = data_url
        self.sensor_id = sensor_id
        self.sensor_pose = sensor_pose

    def add_sensor_pose(self, sensor_pose: SensorPose):
        assert type(sensor_pose) is SensorPose
        self.sensor_pose = sensor_pose
