def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def get_operations():
    while True:
        choice = input("""
+
-
*
/
Pick an operation: """)
        if choice == "+" or choice == "-" or choice == "*" or choice ==  "/":
            return choice
        else:
            print("Invalid choice! try again!")

def calculator(number):
    operation = get_operations()
    number2 = float(input("What's the next number?: "))
    if operation == "+":
        result = add(number, number2)
    elif operation == "-":
        result = sub(number, number2)
    elif operation == "*":
        result = mul(number, number2)
    else:
        result = div(number, number2)
    print(f"{number} {operation} {number2} = {result}")
    while True:
        choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")
        if choice == 'y':
            calculator(result)
        elif choice == 'n':
            new_calculator()
        else:
            print("Invalid choice! try again!")

def new_calculator():
    number1 = float(input("What's the first number?: "))
    calculator(number1)

from art import logo

print(logo)

new_calculator()
