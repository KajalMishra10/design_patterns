
from CouponFactory import CouponFactory


class CouponService:
    def __init__(self):
        self.coupons = {}

    def add_coupon(self, code, discount_percentage, coupon_type):
        self.couponFactory = CouponFactory()
        coupon = self.couponFactory.create_coupon(coupon_type, code=code, discount_percentage=discount_percentage)
        self.coupons[code] = coupon

    def apply_coupon(self, code, cart):
        if code in self.coupons:
            self.coupons[code].apply(cart)
            return f"Coupon {code} applied."
        else:
            return f"Coupon {code} not found."
        
    def remove_coupon(self, code):
        if code in self.coupons:
            del self.coupons[code]
            return f"Coupon {code} removed."
        else:
            return f"Coupon {code} not found."
        
    def list_coupons(self):
        return self.coupons
    
    