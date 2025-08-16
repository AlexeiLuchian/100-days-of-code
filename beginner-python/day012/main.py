from art import logo
from random import randint

def get_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("invalid input!")
        return get_difficulty()

def make_guess(attempts):
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = input("Make a guess: ")
    flag = 0 #Easter Egg
    while not guess.isnumeric():
        flag = 1
        guess = input("That's not a number bro! Now make a normal guess: ")
    if flag:
        print("Good boy!")
    return int(guess)

def check_number(guess, number):
    if guess < number:
        print("Too low")
        print("Go again.\n")
        return 0
    elif guess > number:
        print("Too high")
        print("Go again.\n")
        return 0
    else:
        print(f"You got it! The answer was {number}")
        return 1

def start_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 101)
    attempts = get_difficulty()
    while attempts:
        guess = make_guess(attempts)
        win = check_number(guess, number)
        attempts -= 1
        if win:
            break
    if attempts == 0:
        print(f"You lost, the number was {number}.")

start_game()