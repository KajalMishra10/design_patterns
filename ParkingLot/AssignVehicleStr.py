class assignVehicleStr:

    def assign(self, parking_lot, vehicle):
        pass

class nearestVehicleStr(assignVehicleStr):

    def assign(self, parking_lot, vehicle):
        available_spot = parking_lot.find_available_spot(vehicle)
        return available_spot


