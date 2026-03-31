from ParkingLot import ParkingLot
from VehicleLevel import VehicleLevel
from VehicleSpot import VehicleSpot
from Vehicle import Vehicle
from Entry import Entry
from Exit import Exit
from AssignVehicleStr import nearestVehicleStr
from BillingStrategy import FixedRateBillingStrategy

ParkingLot1 = ParkingLot("Central Parking")

print(ParkingLot1.name)  # Output: Central Parking

VehicleSpot1 = VehicleSpot("A1", "Compact")
VehicleSpot2 = VehicleSpot("A2", "Large")
print(VehicleSpot1.spot_id)  # Output: A1
print(VehicleSpot1.spot_type)  # Output: Compact

VehicleLevel1 = VehicleLevel("Level 1")
VehicleLevel1.add_parking_spot(VehicleSpot1)
VehicleLevel1.add_parking_spot(VehicleSpot2)
print(VehicleLevel1.level_number)  # Output: Level 1

ParkingLot1.add_level(VehicleLevel1)
print(ParkingLot1.levels[0].level_number)  # Output: Level 1

assign_strategy = nearestVehicleStr()
billing_strategy = FixedRateBillingStrategy(50)  # 50 per hour

Entry1 = Entry("Entry 1", ParkingLot1, assign_strategy)
Exit1 = Exit("Exit 1", ParkingLot1, billing_strategy)
ParkingLot1.add_entry_gate(Entry1)
ParkingLot1.add_exit_gate(Exit1)

Vehicle1 = Vehicle("Compact", "MH-12-AB-1234")
ticket = Entry1.generate_ticket(Vehicle1)
print(ticket.entry_time)  # Output: current datetime

fee = Exit1.process_exit(ticket)
print(fee)  # Output: calculated fee

