
from datetime import datetime

from Payment import PaymentFactory
from Ticket import Ticket

class ParkingService:
    def __init__(self, parking_lot, parking_strategy, fee_strategy):
        self.parking_lot = parking_lot
        self.parking_strategy = parking_strategy
        self.fee_strategy = fee_strategy

    def park_vehicle(self, vehicle):
        floors= self.parking_lot.parking_floors
        ParkingStrategy = self.parking_strategy
        spot = ParkingStrategy.find_parking_spot(floors, vehicle)
        if spot:
            spot.occupy_spot()
            print(f"Vehicle parked at Floor, Spot {spot.spot_id}")
            return Ticket(vehicle.vehicle_number, vehicle, spot, entry_time=datetime.now())
        print("No available spot for the vehicle")
        return None
    
    def exit_vehicle(self, ticket,payment_method):
        ticket.exit_time = datetime.now()
        fee_strategy = self.fee_strategy
        ticket.fee = fee_strategy.calculate_fee(ticket)
        print(f"Vehicle {ticket.vehicle.vehicle_number} exited. Fee: {ticket.fee}")
        payment = PaymentFactory.create_payment('India',ticket.fee,payment_method,self.parking_lot.gullak)
        if payment.process_payment():

            ticket.parking_spot.vacate_spot()

            print(
            f"Vehicle {ticket.vehicle.vehicle_number} exited. "
            f"Fee: {ticket.fee}"
            )

            return ticket.fee

        print("Payment failed")
        return None
    
    def add_parking_strategy(self, parking_strategy):
        self.parking_strategy = parking_strategy

    def add_fee_strategy(self, fee_strategy):
        self.fee_strategy = fee_strategy

