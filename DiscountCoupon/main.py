from Cart import Cart
from CouponService import CouponService
from Product import Product

couponService = CouponService()
couponService.add_coupon("SAVE10", 10, "percentage")

product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)

cart = Cart()
cart.add_item(product1, 1)
cart.add_item(product2, 2)

print("Before coupon:")
print(cart)
print()

result = couponService.apply_coupon("SAVE10", cart)
print(result)
print("After coupon:")
print(cart)
