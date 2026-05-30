from ParkingLot import ParkingLot
from ParkingFloor import ParkingFloor
from ParkingSpot import ParkingSpot
from ParkingService import ParkingService
from Ticket import Ticket
from ParkingStrategy import NearestParkingStrategy, BestFitParkingStrategy
from FeeStrategy import FlatFeeStrategy, HourlyFeeStrategy, vehicleTypeFeeStrategy
from Gate import EntryGate, ExitGate
from Vehicle import Vehicle
from Gullak import Gullak
#from Payment import PaymentFactory


parkingLot = ParkingLot("City Center Parking", '102 gali')
ParkingFloor1 = ParkingFloor(1)
ParkingFloor2 = ParkingFloor(2)

ParkingSpot1 = ParkingSpot(1, "Small",False,1)
ParkingSpot2 = ParkingSpot(2, "Large",False,3)
ParkingSpot3 = ParkingSpot(3, "Medium",False,2)
ParkingSpot4 = ParkingSpot(4, "Large",False,3)
ParkingSpot5 = ParkingSpot(5, "Small",False,1)

ParkingFloor1.add_parking_spot(ParkingSpot1)
ParkingFloor1.add_parking_spot(ParkingSpot2)
ParkingFloor2.add_parking_spot(ParkingSpot3)
ParkingFloor2.add_parking_spot(ParkingSpot4)
ParkingFloor2.add_parking_spot(ParkingSpot5)

parkingLot.add_parking_floor(ParkingFloor1)
parkingLot.add_parking_floor(ParkingFloor2)

vehicle1 = Vehicle("KA-01-AB-1234", "Medium",2)
vehicle2 = Vehicle("KA-01-XY-5678", "Small",1)

parking_strategy = NearestParkingStrategy()
fee_strategy = FlatFeeStrategy(20)


parking_service = ParkingService(parkingLot, parking_strategy, fee_strategy)

entry_gate = EntryGate(1,parking_service)
exit_gate = ExitGate(1,parking_service)
parkingLot.add_entry_gate(entry_gate)
parkingLot.add_exit_gate(exit_gate)

gullak = Gullak()
gullak.add_amount(100)
print(f"Gullak balance: {gullak.get_balance()}")
parkingLot.addGullak(gullak)


parkingLot.entry_gates[0].scan_vehicle(vehicle1)
ticket1 = parkingLot.entry_gates[0].park_vehicle(vehicle1)
parkingLot.entry_gates[0].scan_vehicle(vehicle2)
ticket2 = parkingLot.entry_gates[0].park_vehicle(vehicle2)

parkingLot.exit_gates[0].scan_ticket(ticket1)
parkingLot.exit_gates[0].exit_vehicle(ticket1,'Card')

parkingLot.exit_gates[0].scan_ticket(ticket2)
parkingLot.exit_gates[0].exit_vehicle(ticket2,'Cash')