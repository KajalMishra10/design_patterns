class ParkingSpot:
    def __init__(
        self,
        spot_id,
        spot_type,
        is_occupied=False
    ):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = is_occupied

    def occupy_spot(self):
        self.is_occupied = True

    def vacate_spot(self):
        self.is_occupied = False

    def is_available(self):
        return not self.is_occupied
    
