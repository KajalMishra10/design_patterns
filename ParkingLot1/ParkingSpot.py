class ParkingSpot:
    def __init__(
        self,
        spot_id,
        spot_type,
        is_occupied=False,
        size=None
    ):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = is_occupied
        self.size=size

    def occupy_spot(self):
        self.is_occupied = True

    def vacate_spot(self):
        self.is_occupied = False

    def is_available(self):
        return not self.is_occupied
    
    def can_fit_vehicle(self, vehicle):
        if vehicle.size > self.size:
            return False
        if vehicle.size<= self.size and self.spot_type == vehicle.vehicle_type:
            return True
        return False
    