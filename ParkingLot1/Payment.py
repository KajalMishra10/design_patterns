class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        pass


class CashPayment(Payment):
    def __init__(self, amount,Gullak):
        super().__init__(amount)
        self.Gullak = Gullak

    def process_payment(self):
        self.Gullak.add_amount(self.amount)  
        print(f"Processing cash payment of {self.amount}.")
        return True


class OnlinePayment(Payment):
    def __init__(self, amount,Gateway):
        super().__init__(amount)
        self.Gateway = Gateway

    def process_payment(self):
        self.Gateway.process_payment()
        print(f"Processing online payment of {self.amount} through {self.Gateway.name}.")
        return True

class Gullak:
    def __init__(self):
        self.total_amount = 0

    def add_amount(self, amount):
        self.total_amount += amount
        print(f"Added {amount} to Gullak. Total amount: {self.total_amount}.")


class PaymentGateway:
    def __init__(self, name):
        self.name = name

    def process_payment(self):
        pass

class Razorpay(PaymentGateway):
    def __init__(self):
        super().__init__("Razorpay")

    def process_payment(self):
        print(f"Processing payment through {self.name}.")
        return True
        
class PayPal(PaymentGateway):
    def __init__(self):
        super().__init__("PayPal")

    def process_payment(self):
        print(f"Processing payment through {self.name}.")
        return True

class GatewayFactory:
    @staticmethod
    def create_gateway(country):
        if country == "India":
            return Razorpay()
        else:
            return PayPal()
        
class PaymentFactory:
    @staticmethod
    def create_payment(country,amount, method, Gullak=None):
        if method == "cash":
            return CashPayment(amount, Gullak)
        else:
            gateway = GatewayFactory.create_gateway(country)
            return OnlinePayment(amount, gateway)

        