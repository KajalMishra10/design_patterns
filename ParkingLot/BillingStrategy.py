class BillingStrategy:
    def calculate_bill(self, entry_time, exit_time, vehicle_type=None):
        raise NotImplementedError("Subclasses must implement this method")
    
class FixedRateBillingStrategy(BillingStrategy):
    def __init__(self, rate_per_hour):
        self.rate_per_hour = rate_per_hour
        
    def calculate_bill(self, entry_time, exit_time, vehicle_type=None):
        duration = (exit_time - entry_time).total_seconds() / 3600  # Convert to hours
        return self.rate_per_hour * duration
    
class VehicleTypeBillingStrategy(BillingStrategy):
    def __init__(self, rates):
        self.rates = rates  # Dictionary mapping vehicle types to rates
        
    def calculate_bill(self, entry_time, exit_time, vehicle_type):
        duration = (exit_time - entry_time).total_seconds() / 3600  # Convert to hours
        rate_per_hour = self.rates.get(vehicle_type, 0)  # Get rate for the vehicle type
        return rate_per_hour * duration