from api.internal_models.transport import Transport
from api.internal_models.point import Point


class Route:
    def __init__(self, transport, points):
        self.transport = Transport(transport)
        self.points = []
        for p in points:
            self.points.append(Point(p))
