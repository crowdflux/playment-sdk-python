class SensorMeta:
    def __init__(self, _id: str, name: str, primary_view: bool, state: str = "editable"):
        self.id = _id
        self.name = name
        self.primary_view = primary_view
        self.state = state
