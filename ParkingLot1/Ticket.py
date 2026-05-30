class Ticket:
    def __init__(self, ticket_id, vehicle, parking_spot, entry_time):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_time = entry_time
        self.exit_time = None
        self.fee = None
    
    