from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

while nr_letters:
    password.append(letters[randint(0, len(letters)-1)])
    nr_letters -= 1
while nr_symbols:
    password.append(symbols[randint(0, len(symbols)-1)])
    nr_symbols -=1
while nr_numbers:
    password.append(numbers[randint(0, len(numbers)-1)])
    nr_numbers -=1

print(password)

for index in range(len(password)):
    random = randint(0,len(password)-1)
    aux = password[random]
    password[random] = password[index]
    password[index] = aux

print(password)

string = ""
for char in password:
    string += char

print("Your password is:", string)