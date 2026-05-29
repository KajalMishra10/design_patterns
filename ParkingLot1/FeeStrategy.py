class FeeStrategy:
    def calculate_fee(self, ticket):
        pass

class FlatFeeStrategy(FeeStrategy):
    def __init__(self, flat_fee):
        self.flat_fee = flat_fee

    def calculate_fee(self, ticket):
        return self.flat_fee
    
class HourlyFeeStrategy(FeeStrategy):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def calculate_fee(self, ticket):
        hours_parked = (ticket.exit_time - ticket.entry_time).total_seconds() / 3600
        return self.hourly_rate * hours_parked
    
class vehicleTypeFeeStrategy(FeeStrategy):
    def __init__(self, rates):
        self.rates = rates  # Dictionary mapping vehicle types to rates

    def calculate_fee(self, ticket):
        vehicle_type = ticket.vehicle.vehicle_type
        rate = self.rates.get(vehicle_type, 0)
        hours_parked = (ticket.exit_time - ticket.entry_time).total_seconds() / 3600
        return rate * hours_parked