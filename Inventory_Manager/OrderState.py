from abc import ABC, abstractmethod


class OrderState(ABC):
    """Base state — har state ye methods implement karegi"""

    @abstractmethod
    def confirm(self, order):
        pass

    @abstractmethod
    def dispatch(self, order):
        pass

    @abstractmethod
    def deliver(self, order):
        pass

    @abstractmethod
    def cancel(self, order):
        pass


class PlacedState(OrderState):
    """Order abhi place hua — confirm ya cancel ho sakta hai"""

    def confirm(self, order):
        print(f"[Order] Confirmed! Preparing items...")
        order.set_state(ConfirmedState())

    def dispatch(self, order):
        print("[Order] Cannot dispatch — order not confirmed yet")

    def deliver(self, order):
        print("[Order] Cannot deliver — order not even dispatched")

    def cancel(self, order):
        print(f"[Order] Cancelled from PLACED state. Restoring inventory...")
        order.restore_inventory()
        order.free_delivery_partner()
        order.set_state(CancelledState())

    def __repr__(self):
        return "PLACED"


class ConfirmedState(OrderState):
    """Order confirmed — dispatch ya cancel ho sakta hai"""

    def confirm(self, order):
        print("[Order] Already confirmed")

    def dispatch(self, order):
        print(f"[Order] Dispatched! {order.delivery_partner.name} is on the way")
        order.set_state(DispatchedState())

    def deliver(self, order):
        print("[Order] Cannot deliver — not dispatched yet")

    def cancel(self, order):
        print(f"[Order] Cancelled from CONFIRMED state. Restoring inventory...")
        order.restore_inventory()
        order.free_delivery_partner()
        order.set_state(CancelledState())

    def __repr__(self):
        return "CONFIRMED"


class DispatchedState(OrderState):
    """Order dispatched — sirf deliver ho sakta hai, cancel NAHI"""

    def confirm(self, order):
        print("[Order] Already confirmed and dispatched")

    def dispatch(self, order):
        print("[Order] Already dispatched")

    def deliver(self, order):
        print(f"[Order] Delivered! {order.delivery_partner.name} completed delivery")
        order.free_delivery_partner()
        order.set_state(DeliveredState())

    def cancel(self, order):
        print("[Order] Cannot cancel — already dispatched!")

    def __repr__(self):
        return "DISPATCHED"


class DeliveredState(OrderState):
    """Order delivered — kuch nahi ho sakta ab"""

    def confirm(self, order):
        print("[Order] Already delivered")

    def dispatch(self, order):
        print("[Order] Already delivered")

    def deliver(self, order):
        print("[Order] Already delivered")

    def cancel(self, order):
        print("[Order] Cannot cancel — already delivered!")

    def __repr__(self):
        return "DELIVERED"


class CancelledState(OrderState):
    """Order cancelled — kuch nahi ho sakta ab"""

    def confirm(self, order):
        print("[Order] Cannot confirm — order is cancelled")

    def dispatch(self, order):
        print("[Order] Cannot dispatch — order is cancelled")

    def deliver(self, order):
        print("[Order] Cannot deliver — order is cancelled")

    def cancel(self, order):
        print("[Order] Already cancelled")

    def __repr__(self):
        return "CANCELLED"
