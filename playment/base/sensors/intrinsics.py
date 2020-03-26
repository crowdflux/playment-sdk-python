class Intrinsics:
    def __init__(self, cx: float, cy: float, fx: float, fy: float, k1: float, k2: float,
                 k3: float, k4: float, p1: float, p2: float, skew: float, scale_factor: float):
        assert type(cx) is float
        assert type(cy) is float
        assert type(fx) is float
        assert type(fy) is float
        assert type(k1) is float
        assert type(k2) is float
        assert type(k3) is float
        assert type(k4) is float
        assert type(p1) is float
        assert type(p2) is float
        assert type(skew) is float
        assert type(scale_factor) is float
        self.cx = cx
        self.cy = cy
        self.fx = fx
        self.fy = fy
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.p1 = p1
        self.p2 = p2
        self.skew = skew
        self.scale_factor = scale_factor
