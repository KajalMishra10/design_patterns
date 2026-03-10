import User
import Restraurant
import OrderService
import Payment
service = User.UserService()
start = service.add_user('mishra', 'k@gmail.com')
#start=User.UserService.add_user('mishra','k@gmail.com')
rest=Restraurant.RestaurantService()
rest.displayRestaurants()

#UserService.rest.restaurants[User0]
start.cart.restaurant=rest.restaurants[0]
print(start.cart.restaurant.name)
menu=rest.restaurants[0].display_menu()
start.cart.addItem(menu[0])
start.cart.addItem(menu[1])

order1=OrderService.OrderManager()

#order=order1.Order()
payment=Payment.CreditCardPayment(12345678,'kajal',10/11/2000)
print(start.cart.restaurant)
order=order1.place_order(start.cart,payment,start.cart.restaurant)
order.place_order(start.cart,payment,start.cart.restaurant)

order.state.prepare_order(order)
order.state.deliver_order(order)
order.state.complete_order(order)
order.state.place_order(order)