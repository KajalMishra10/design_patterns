from enums.direction import Direction

class TrafficPhase:

    def __init__(
        self,
        active_directions:list[Direction],
        green_duration:int,
        yellow_duration:int
    ):
        self.active_directions = active_directions
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration