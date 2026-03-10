from DeliveryService import RandomDeliveryAgentAssignment, DeliveryService

# ------------------ STATE BASE CLASS ------------------

class State:
    def place_order(self, order, cart, payment_method, restaurant):
        print("Action not allowed in current state.")

    def cancel_order(self, order):
        print("Action not allowed in current state.")

    def prepare_order(self, order):
        print("Action not allowed in current state.")

    def deliver_order(self, order):
        print("Action not allowed in current state.")

    def complete_order(self, order):
        print("Action not allowed in current state.")


# ------------------ ORDER CONTEXT ------------------
class OrderManager:
   
    def place_order(self, cart, payment_method, restaurant):
        

        

        if restaurant.canAddOrder():
            print("placed order")
            self.order=Order()
            self.order.place_order(cart, payment_method, restaurant)
            return self.order
            #order.state = ProcessingOrder()
            #order.state.prepare_order(order)
        else:
            print('hi hi')
            order.state = CancelledOrder().cancel_order(order)

class Order:
    def __init__(self):
        self.items = []
        self.total = 0.0
        self.state = PendingOrder()

    # Delegation to current state
    def place_order(self, cart, payment_method, restaurant):
        self.state.place_order(self, cart, payment_method, restaurant)

    def cancel_order(self):
        self.state.cancel_order(self)

    def prepare_order(self):
        self.state.prepare_order(self)

    def deliver_order(self):
        self.state.deliver_order(self)

    def complete_order(self):
        self.state.complete_order(self)


# ------------------ STATES ------------------

class PendingOrder(State):
    def place_order(self, order, cart, payment_method, restaurant):
        order.items = cart.items
        order.total = cart.total

        print("Order placed successfully!")
        print(f"Total amount: ${order.total:.2f}")

        

        #if restaurant.canAddOrder(order):
           # payment_method.process_payment(order.total)
            
        order.state = ProcessingOrder()
            #order.state.prepare_order(order)
       
        #order.state = CancelledOrder().cancel_order(order)

    def cancel_order(self, order):
        print("Order cancelled.")
        order.state = CancelledOrder()


class ProcessingOrder(State):
    def prepare_order(self, order):
        print("Order is being prepared.")
        order.state = PreparedOrder()
        #order.state.deliver_order(order)
        return self

    def cancel_order(self, order):
        print("Order cancelled while processing.")
        order.state = CancelledOrder()


class PreparedOrder(State):
    def deliver_order(self, order):
        print("Order is out for delivery.")
        order.state = DeliveredOrder()
       # order.state.complete_order(order)

    def cancel_order(self, order):
        print("Cannot cancel. Order already prepared.")


class DeliveredOrder(State):
    def complete_order(self, order):
        strategy=DeliveryService(RandomDeliveryAgentAssignment()) 
        strategy.assign_delivery(order)
        print("Order completed successfully!")
        order.state = CompletedOrder()


class CompletedOrder(State):
    def place_order(self, order):
        print("Order delivery completed. ")


class CancelledOrder(State):
    def place_order(self, order, cart, payment_method, restaurant):
        print("Order was cancelled. Create a new order.")

