from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_mkr = CoffeeMaker()
money_mac = MoneyMachine()
is_on = True
# coffee_mkr.report()
# money_mac.report()
while is_on:
    options = menu.get_items()
    order = input(f"What would you like to have? ({options})")
    if order == 'OFF':
        is_on = False
    elif order == 'Report':
        coffee_mkr.report()
        money_mac.report()
    else:
        order_name = menu.find_drink(order)
        if coffee_mkr.is_resource_sufficient(order_name) and money_mac.make_payment(order_name.cost):
            coffee_mkr.make_coffee(order_name)

