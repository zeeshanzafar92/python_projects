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
machine_resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100
}
cash = 0


def print_report(coffee_machine, cash):
    for i in machine_resources:
        print(f"{i} = {machine_resources[i]}")
    print(f"💲 = {cash}")


def sufficient_resources(coffee, resources):
    for i in coffee["ingredients"]:
        if resources[i] < coffee["ingredients"][i]:
            print(f"Not enough {i}")
        return False


def resource_cost(coffee, machine_resources):
    for i in coffee["ingredients"]:
        remaining = machine_resources[i] - coffee["ingredients"][i]
        machine_resources[i] = remaining
    return machine_resources


def process_coins(coffee_price):
    print(f"it will cost you 💲{coffee_price}. Please insert 🪙 to process")
    total = int(input("Please insert quarters: ")) * 0.25
    total += int(input("Please insert dimes: ")) * 0.10
    total += int(input("Please insert nickles: ")) * 0.05
    total += int(input("Please insert pennies: ")) * 0.01
    return round(total, 2)


def process_transaction(money_received, coffee_price):
    if money_received == coffee_price:
        print("Transaction Successful")
        return True
    elif money_received > coffee_price:
        change = money_received - coffee_price
        print(f"Transaction Successful, Here's 💲{change} change")
        return True
    else:
        print("Sorry, not enough 💲. 💵 refunded.")
        return False


is_on = True
while is_on:
    user_choice = input("What would you like? Espresso, Cappuccino, Latte: ").lower()
    if user_choice == "report":
        print(print_report(machine_resources, cash))
    elif user_choice == "off":
        is_on = False
    else:
        coffee = MENU[user_choice]
        coffee_price = coffee["cost"]
        if not sufficient_resources(coffee, machine_resources):
            money_received = process_coins(coffee_price)
            transaction_success = process_transaction(money_received, coffee_price)
            if transaction_success:
                cash += coffee_price
                resource_cost(coffee, machine_resources)
                print(f"Here's your hot 🍵")


