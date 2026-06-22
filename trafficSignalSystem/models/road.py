from enums.direction import Direction

class Road:

    def __init__(
        self,
        road_id:int,
        direction:Direction
    ):
        self.road_id = road_id
        self.direction = direction