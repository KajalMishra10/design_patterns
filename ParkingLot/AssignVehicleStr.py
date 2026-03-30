class assignVehicleStr:
   
        
    def assign(self, parking_spot):
        pass

class nearestVehicleStr(assignVehicleStr):
    
        
    def assign(self, parking_lot, vehicle):
        nearest_spot = parking_lot.find_nearest_available_spot()
        if nearest_spot:
            nearest_spot.assign_vehicle(vehicle)


