class Coupons:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount

    def apply_coupon(self, total_amount):
       pass

class PercentageCoupon(Coupons):
    def __init__(self, code, discount):
        super().__init__(code, discount)

    def apply_coupon(self, total_amount):
        discount_amount = total_amount * (self.discount / 100)
        new_total = total_amount - discount_amount
        print(f"Applying {self.discount}% coupon. Discount amount: ${discount_amount:.2f}. New total: ${new_total:.2f}")
        return new_total
    
class FixedAmountCoupon(Coupons):
    def __init__(self, code, discount):
        super().__init__(code, discount)

    def apply_coupon(self, total_amount):
        new_total = max(0, total_amount - self.discount)
        print(f"Applying ${self.discount:.2f} coupon. New total: ${new_total:.2f}")
        return new_total

class CouponManager:
    def __init__(self):
        self.coupons = {}

    def add_coupon(self, coupon):
        self.coupons[coupon.code] = coupon
        print(f"Coupon {coupon.code} added successfully.")

    def apply_coupon(self, code, total_amount):
        if code in self.coupons:
            return self.coupons[code].apply_coupon(total_amount)
        else:
            print(f"Coupon code {code} not found. No discount applied.")
            return total_amount
    
    