from playment.sensors.intrinsics import Intrinsics


class SensorMeta:
    def __init__(self, _id: str, name: str, primary_view: bool, modality: str = None,
                 state: str = "editable", intrinsics: Intrinsics = None):
        self.id = _id
        self.name = name
        self.primary_view = primary_view
        self.modality = modality
        self.state = state
        self.intrinsics = intrinsics

    def add_intrinsics(self, intrinsics: Intrinsics):
        self.intrinsics = intrinsics
