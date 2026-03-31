from datetime import datetime


class Exit:
    def __init__(self, exit_id, parking_lot, billing_strategy):
        self.exit_id = exit_id
        self.parking_lot = parking_lot
        self.billing_strategy = billing_strategy

    def process_exit(self, ticket):
        if ticket.exit_time is None:
            ticket.set_exit_time(datetime.now())
            fee = self.billing_strategy.calculate_bill(ticket.entry_time, ticket.exit_time, ticket.vehicle_info.type)
            self.parking_lot.free_spot(ticket.vehicle_spot_id)
            return fee
        else:
            print("This ticket has already been processed for exit.")
            return None