class Gate:
    def __init__(self, gate_id, gate_type):
        self.gate_id = gate_id
        self.gate_type = gate_type  # Entry or Exit
  

class EntryGate(Gate):
    def __init__(self, gate_id,parking_service):
        super().__init__(gate_id, "Entry")
        self.parking_service = parking_service

    def scan_vehicle(self, vehicle):
        print(f"Scanning vehicle {vehicle.vehicle_number} at Entry Gate {self.gate_id}")
        return vehicle
    
    def park_vehicle(self, vehicle):
        ticket = self.parking_service.park_vehicle(vehicle)
        if ticket:
            print(f"Vehicle {vehicle.vehicle_number} parked successfully. Ticket ID: {ticket.ticket_id}")
            return ticket
        else:
            print(f"Failed to park vehicle {vehicle.vehicle_number}. No available spots.")
            return None

    

class ExitGate(Gate):
    def __init__(self, gate_id,parking_service):
        super().__init__(gate_id, "Exit")
        self.parking_service = parking_service

    def scan_ticket(self, ticket):
        print(f"Scanning ticket {ticket.ticket_id} at Exit Gate {self.gate_id}")
        return ticket
    
    def exit_vehicle(self, ticket,payment_method):
        fee = self.parking_service.exit_vehicle(ticket,payment_method)
        if fee is not None:
            print(f"Vehicle {ticket.vehicle.vehicle_number} exited successfully. Fee: {fee}")
            return fee
        else:
            print(f"Failed to exit vehicle {ticket.vehicle.vehicle_number}. Payment failed.")
            return None

    