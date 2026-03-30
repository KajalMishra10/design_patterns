class VehicleLevel:
    def __init__(self, level_number):
        self.level_number = level_number
        self.parking_spots = []  # List of parking spots on this level

    def add_parking_spot(self, parking_spot):
        self.parking_spots.append(parking_spot)

    def get_available_spots(self, vehicle_type=None):
        if vehicle_type is None:
            return [spot for spot in self.parking_spots if spot.is_occupied == False]
        else:
            return [spot for spot in self.parking_spots if spot.is_occupied == False and spot.spot_type == vehicle_type]