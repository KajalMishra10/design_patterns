class ParkingLot:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, "initialized"):  # prevent re-init
            self.name = name
            self.levels = []
            self.entry_gates = []
            self.exit_gates = []
            self.initialized = True

    def add_level(self, level):
        self.levels.append(level)

    def add_entry_gate(self, entry_gate):
        self.entry_gates.append(entry_gate)

    def add_exit_gate(self, exit_gate):
        self.exit_gates.append(exit_gate)

    def find_available_spot(self, vehicle):
        for level in self.levels:
            available_spots = level.get_available_spots(vehicle.type)
            if available_spots:
                return available_spots[0]
        return None

    def free_spot(self, spot_id):
        for level in self.levels:
            for spot in level.parking_spots:
                if spot.spot_id == spot_id:
                    spot.remove_vehicle()
                    return True
        return False
    