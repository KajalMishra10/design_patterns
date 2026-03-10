from Coupon import Coupon, BankCoupon, SeasonalCoupon, LoyaltyCoupon
from DiscountStrategy import PercentageDiscount, FixedAmountDiscount


class CouponFactory:
    @staticmethod
    def create_coupon(coupon_type, **kwargs):
        if coupon_type == "percentage":
            strategy = PercentageDiscount(kwargs['discount_percentage'])
            return Coupon(kwargs['code'], strategy)
        elif coupon_type == "fixed":
            strategy = FixedAmountDiscount(kwargs['discount_amount'])
            return Coupon(kwargs['code'], strategy)
        elif coupon_type == "bank":
            strategy = PercentageDiscount(kwargs['discount_percentage'])
            return BankCoupon(kwargs['code'], strategy)
        elif coupon_type == "seasonal":
            strategy = PercentageDiscount(kwargs['discount_percentage'])
            return SeasonalCoupon(kwargs['code'], strategy)
        elif coupon_type == "loyalty":
            strategy = PercentageDiscount(kwargs['discount_percentage'])
            return LoyaltyCoupon(kwargs['code'], strategy)
        else:
            raise ValueError(f"Invalid coupon type: {coupon_type}")
