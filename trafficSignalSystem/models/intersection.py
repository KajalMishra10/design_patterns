from models.road import Road
from models.traffic_light import TrafficLight

class Intersection:

    def __init__(
        self,
        intersection_id:int,
        roads:list[Road],
        lights:list[TrafficLight]
    ):
        self.id = intersection_id
        self.roads = roads
        self.lights = lights