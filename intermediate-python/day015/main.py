from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

def show_resources():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")

def check_resources(user_choice):
    for resource in resources:
        if resources[resource] < MENU[user_choice]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True

def get_coins():
    quarters = float(input("Insert the number of quarters: "))
    nickles = float(input("Insert the number of nickles: "))
    dimes = float(input("Insert the number of dimes: "))
    pennies = float(input("Insert the number of pennies: "))
    return quarters*0.25 + nickles*0.1 + dimes*0.05 + pennies*0.01
 
def start_machine():
    machine_on = True
    while machine_on:
        user_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice in MENU:
            if check_resources(user_choice):
                coins = get_coins()
                if coins >= MENU[user_choice]["cost"]:
                    if coins > MENU[user_choice]["cost"]:
                        print(f"Here is ${round(coins - MENU[user_choice]["cost"],2)} in change.")
                    print("all good")
                    print(f"🫘  Your {user_choice} is being prepared! 🫘")
                else:
                    print("Sorry that's not enough money. Money refunded. 💰")
        elif user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            show_resources()
        else:
            print("⛔ We don't have that in our menu ⛔")

start_machine()