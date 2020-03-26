from playment.base.sensors.intrinsics import Intrinsics


class Sensor:
    def __init__(self, _id: str, name: str, primary_view: bool, modality: str = None,
                 state: str = "editable", intrinsics: Intrinsics = None):
        assert type(_id) is str
        assert type(name) is str
        assert type(primary_view) is str
        assert type(modality) is str
        assert type(intrinsics) is Intrinsics or None
        assert state == "editable" or "non_editable"
        self.id = _id
        self.name = name
        self.primary_view = primary_view
        self.modality = modality
        self.state = state
        self.intrinsics = intrinsics

    def add_intrinsics(self, intrinsics: Intrinsics):
        assert type(intrinsics) is Intrinsics
        self.intrinsics = intrinsics
