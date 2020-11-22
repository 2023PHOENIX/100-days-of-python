from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

""" 
print report
check resources are sufficient 
process coins 

"""
money_machine = MoneyMachine()

money_machine.report()

coffee = CoffeeMaker()
coffee.report()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee.make_coffee(drink)
