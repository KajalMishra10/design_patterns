class Ticket:
    def __init__(self, ticket_id, Vehicle, entry_time, vehicle_spot_id):
        self.ticket_id = ticket_id
        self.vehicle_info = Vehicle
        self.entry_time = entry_time
        self.vehicle_spot_id = vehicle_spot_id
        self.exit_time = None

        
    def set_exit_time(self, exit_time):
        self.exit_time = exit_time
        
    def get_ticket_info(self):
        return f"Ticket ID: {self.ticket_id}, Vehicle Info: {self.vehicle_info}, Entry Time: {self.entry_time}, Vehicle Spot ID: {self.vehicle_spot_id}, Exit Time: {self.exit_time}"