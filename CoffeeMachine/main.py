work = True
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


def coin():
    print("Please insert coins.")
    coins_Q = int(input("How many Quarters?: "))
    coins_D = int(input("How many Dime?: "))
    coins_N = int(input("How many Nickel?: "))
    coins_P = int(input("How many Penny?: "))
    total_coins = float(coins_Q * 0.25 + coins_D * 0.1 + coins_N * 0.05 + coins_P * 0.01)
    return total_coins


while work:
    user_input = input("What would you like? (Espresso/Latte/Cappuccino): ")
    if user_input == 'Espresso':
        if resources["water"] < 50:
            print("Insufficient water. Please refill.")
        elif resources["coffee"] < 18:
            print("Insufficient coffee. Please refill.")
        else:
            coins_input = coin()
            change = round(coins_input - 1.5, 2)
            if change < 0:
                print("Sorry! That's not enough. Here's your refund.")
            else:
                print(f"Here's your espresso:☕ & Here's your change: ${change}")
                profit += 1.5
                resources["water"] = resources["water"] - 50
                resources["coffee"] = resources["coffee"] - 18
    elif user_input == 'Latte':
        if resources["water"] < 200:
            print("Insufficient water. Please refill.")
        elif resources["coffee"] < 24:
            print("Insufficient coffee. Please refill.")
        elif resources["milk"] < 150:
            print("Insufficient milk. Please refill.")
        else:
            coins_input = coin()
            change = round(coins_input - 2.5, 2)
            if change < 0:
                print("Sorry! That's not enough. Here's your refund.")
            else:
                print(f"Here's your latte:☕ & Here's your change: ${change} ")
                profit += 2.5
                resources["water"] = resources["water"] - 200
                resources["coffee"] = resources["coffee"] - 24
                resources["milk"] = resources["milk"] - 150
    elif user_input == 'Cappuccino':
        if resources["water"] < 250:
            print("Insufficient water. Please refill.")
        elif resources["coffee"] < 24:
            print("Insufficient coffee. Please refill.")
        elif resources["milk"] < 100:
            print("Insufficient milk. Please refill.")
        else:
            coins_input = coin()
            change = round(coins_input - 3.0, 2)
            if change < 0:
                print("Sorry! That's not enough. Here's your refund.")
            else:
                print(f"Here's your cappuccino:☕ & Here's your change: ${change}")
                profit += 3.0
                resources["water"] = resources["water"] - 250
                resources["coffee"] = resources["coffee"] - 24
                resources["milk"] = resources["milk"] - 100
    elif user_input == 'OFF':
        work = False
    elif user_input == 'Report':
        for i in resources:
            print(i + " : ")
            print(resources[i])
        print(f"Profit earned: {profit}")

