class Ticket:
    def __init__(self, ticket_id, vehicle_info, entry_time):
        self.ticket_id = ticket_id
        self.vehicle_info = vehicle_info
        self.entry_time = entry_time
        self.exit_time = None
        
    def set_exit_time(self, exit_time):
        self.exit_time = exit_time
        
    def get_ticket_info(self):
        return f"Ticket ID: {self.ticket_id}, Vehicle Info: {self.vehicle_info}, Entry Time: {self.entry_time}, Exit Time: {self.exit_time}"