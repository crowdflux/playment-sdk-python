class Heading:
    def __init__(self, w, x, y, z):
        assert type(w) is float
        assert type(x) is float
        assert type(y) is float
        assert type(z) is float
        self.w = w
        self.x = x
        self.y = y
        self.z = z


class Position:
    def __init__(self, x, y, z):
        assert type(x) is float
        assert type(y) is float
        assert type(z) is float
        self.x = x
        self.y = y
        self.z = z


class SensorPose:
    def __init__(self, heading: Heading, position: Position):
        assert type(heading) is Heading
        assert type(position) is Position
        self.heading = heading
        self.position = position
