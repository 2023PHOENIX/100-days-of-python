# menu dictionary inside dictionary
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order):
    """ returns True  when resources are sufficient"""
    for item in order:
        if order[item] >= resources[item]:
            return False
        return True


def process_coins():
    """returns the total coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes? : ")) * 0.1
    total += int(input("how many nickles? : ")) * 0.05
    total += int(input("how many pennies? : ")) * 0.01

    return total


def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += money_received
        return True
    else:
        print("Sorry that's not enough. Money Refunded")
        return False


def make_coffee(drink_name, order):
    """deduct the required ingredients from the resources"""
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your ☕☕☕☕{drink_name} ☕☕☕☕")


is_on = True

profit = 0

while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino)")

    if choice == "turnoff":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}ml")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink['cost'])
            make_coffee(choice, drink["ingredients"])
