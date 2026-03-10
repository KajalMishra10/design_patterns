class Payment:
    def __init__(self,payment_method):
        self.payment_method=payment_method

    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, card_number, cardholder_name, expiration_date):
        super().__init__("Credit Card")
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.expiration_date = expiration_date
        #self.cvv = cvv

    def process_payment(self, amount):
        print(f"Processing credit card payment for {self.cardholder_name}...")
        # Simulate credit card payment processing logic here
        print("Credit card payment successful!")

class CashPayment(Payment):
    def __init__(self):
        super().__init__("Cash")

    def process_payment(self, amount):
        print(f"Processing cash payment of ${amount:.2f}...")
        # Simulate cash payment processing logic here
        print("Cash payment successful!")