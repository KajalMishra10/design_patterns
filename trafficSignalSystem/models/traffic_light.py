from enums.light_color import LightColor
from models.road import Road

class TrafficLight:

    def __init__(self, road:Road):
        self.road = road
        self.color = LightColor.RED

    def set_color(
        self,
        color:LightColor
    ):
        self.color = color