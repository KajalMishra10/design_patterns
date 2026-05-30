class ParkingStrategy:
    def find_parking_spot(self, parking_floors, vehicle):
        raise NotImplementedError("This method should be implemented by subclasses.")
    
class NearestParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_floors, vehicle):
        for floor in parking_floors:
            for spot in floor.parking_spots:
                if spot.is_available() and spot.can_fit_vehicle(vehicle):
                    return spot
        return None
    
class BestFitParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, parking_floors, vehicle):
        best_spot = None
        for floor in parking_floors:
            for spot in floor.parking_spots:
                if spot.is_available() and spot.can_fit_vehicle(vehicle):
                    if not best_spot or spot.size < best_spot.size:
                        best_spot = spot
        return best_spot