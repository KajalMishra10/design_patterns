class ParkingLot:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.parking_floors = []
        self.floors=0
        self.entry_gates = []
        self.exit_gates = []
        self.gullak = None

    
    def add_parking_floor(self, parking_floor):
        self.parking_floors.append(parking_floor)
    
    def addGullak(self, gullak):
        self.gullak = gullak

    def add_entry_gate(self, entry_gate):
        self.entry_gates.append(entry_gate)

    def add_exit_gate(self, exit_gate):
        self.exit_gates.append(exit_gate)

    