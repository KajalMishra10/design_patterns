class ParkingFloor:
    def __init__(
        self,
        floor_number,
       
    ):
        self.floor_number = floor_number
        self.parking_spots = []

    def add_parking_spot(self, parking_spot):
        self.parking_spots.append(parking_spot)

    def find_available_spot(self, vehicle):
        for spot in self.parking_spots:
            if spot.is_available() and spot.spot_type == vehicle.vehicle_type:
                return spot
        return None
    
    
    