class VehicleSpot:

    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False
        self.vehicle = None

    def park_vehicle(self, vehicle):
        if not self.is_occupied:
            self.vehicle = vehicle
            self.is_occupied = True
            return True
        return False

    def remove_vehicle(self):
        if self.is_occupied:
            self.vehicle = None
            self.is_occupied = False
            return True
        return False