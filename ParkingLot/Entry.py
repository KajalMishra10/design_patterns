#class Entry
# This class represents the entry point of the parking lot. It is responsible for generating tickets for vehicles entering the parking lot and keeping track of the available parking spots.
from datetime import datetime

from Ticket import Ticket


class Entry:
    def __init__(self, entry_id, parking_lot, assign_vehicle_str):
        self.entry_id = entry_id
        self.parking_lot = parking_lot
        self.assign_vehicle_str = assign_vehicle_str

    def generate_ticket(self, vehicle):
        available_spot = self.assign_vehicle_str.assign(self.parking_lot, vehicle)
        if available_spot:
            ticket_id = f"{self.entry_id}-{available_spot.spot_id}"
            ticket = Ticket(ticket_id, vehicle, datetime.now(), available_spot.spot_id)
            available_spot.park_vehicle(vehicle)
            return ticket
        else:
            print("No available spots for this vehicle type.")
            return None