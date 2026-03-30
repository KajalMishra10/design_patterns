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
            self.initialized = True

    def add_level(self, level):
        self.levels.append(level)

    def find_available_spot(self, vehicle):
        for level in self.levels:
            available_spots = level.get_available_spots( vehicle.type)
            if available_spots:
                return available_spots[0]
        return None
    