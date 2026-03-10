class Coupon:
    def __init__(self, code, strategy, next_coupon=None, isCombinable=True):
        self.code = code
        self.strategy = strategy
        self.next_coupon = next_coupon
        self.isCombinable = isCombinable

    def apply(self, cart):
        if self.isApplicable(cart):
            discount_amount = self.strategy.apply_discount(cart.get_total_price())
            cart.apply_discount(discount_amount)

        if self.next_coupon and self.isCombinable:
            self.next_coupon.apply(cart)

    def isApplicable(self, cart):
        return True


class BankCoupon(Coupon):
    def __init__(self, code, strategy, next_coupon=None, isCombinable=True):
        super().__init__(code, strategy, next_coupon, isCombinable)

    def isApplicable(self, cart):
        return True


class SeasonalCoupon(Coupon):
    def __init__(self, code, strategy, next_coupon=None, isCombinable=True):
        super().__init__(code, strategy, next_coupon, isCombinable)

    def isApplicable(self, cart):
        return True


class LoyaltyCoupon(Coupon):
    def __init__(self, code, strategy, next_coupon=None, isCombinable=True):
        super().__init__(code, strategy, next_coupon, isCombinable)

    def isApplicable(self, cart):
        return True