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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


work = True
profit = 0.0


def coin():
    print("Please insert coins.")
    coins_Q = int(input("How many Quarters?: "))
    coins_D = int(input("How many Dime?: "))
    coins_N = int(input("How many Nickel?: "))
    coins_P = int(input("How many Penny?: "))
    total_coins = float(coins_Q * 0.25 + coins_D * 0.1 + coins_N * 0.05 + coins_P * 0.01)
    return total_coins


def coffee_fn(users_input):
    if users_input in MENU:
        if resources["water"] < MENU[users_input]["ingredients"]["water"]:
            print("Insufficient water. Please refill.")
        elif resources["coffee"] < MENU[users_input]["ingredients"]["coffee"]:
            print("Insufficient coffee. Please refill.")
        elif resources["milk"] < MENU[users_input]["ingredients"]["milk"]:
            print("Insufficient milk. Please refill.")
        else:
            coins_input = coin()
            change = round(coins_input - MENU[users_input]["cost"], 2)
            if change < 0:
                print("Sorry! That's not enough. Here's your refund.")
            else:
                print(f"Here's your {users_input}:☕ & Here's your change: ${change}")
                resources["water"] -= MENU[users_input]["ingredients"]["water"]
                resources["coffee"] -= MENU[users_input]["ingredients"]["coffee"]
                resources["milk"] -= MENU[users_input]["ingredients"]["milk"]
                return profit + MENU[users_input]["cost"]
    else:
        return 0


while work:
    #print("Welcome to Shreyanshi's Cafe.")
    user_input = input("Welcome! What would you like? (espresso/latte/cappuccino): ")
    total_profit = coffee_fn(user_input)
    if user_input == 'OFF':
        work = False
    elif user_input == 'Report':
        for i in resources:
            print(i + " : ")
            print(resources[i])
        print(f"Profit earned: {total_profit}")

