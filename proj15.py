from settings import MENU
from settings import resources


def making_coffee(coffee_type, money_amount):
    if money_amount < MENU[coffee_type]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    elif coffee_type != "espresso":
        resources["water"] = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
        print(f"Here is ${round(money_amount - MENU[coffee_type]['cost'], 2)} in change.")
        print(f"Here is your {coffee_type}. Enjoy!")
        return
    else:
        resources["water"] = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
        print(f"Here is ${round(money_amount - MENU[coffee_type]['cost'], 2)  } in change.")
        print(f"Here is your {coffee_type}. Enjoy!")
        return


def coins_calculation():
    print("Please, insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01


def check_resources(chosen_coffee):
    if resources["water"] < MENU[chosen_coffee]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif chosen_coffee != "espresso" and resources["milk"] < MENU[chosen_coffee]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[chosen_coffee]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True


everything_ok = True
while everything_ok:
    users_input = input("What would you like? (espresso/latte/cappuccino): ")
    if users_input == "off":
        everything_ok = False
    elif users_input == "report":
        print(f"Water: {resources.get('water')}ml")
        print(f"Milk: {resources.get('milk')}ml")
        print(f"Coffee: {resources.get('coffee')}g")
    else:
        if check_resources(users_input):
            entered_amount_coins = coins_calculation()
            making_coffee(users_input, entered_amount_coins)

