from art import logo, vs
from game_data import data
from random import randint

def get_person():
    return data[randint(0,len(data)-1)]

def print_info(person_a, person_b):
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(vs)
    print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

def check_answer(u_answer, person_a, person_b):
    if u_answer == "A" and person_a['follower_count'] >= person_b['follower_count']:
        return True
    elif u_answer == "B" and person_b['follower_count'] >= person_a['follower_count']:
        return True
    else:
        return False


def start_game():
    print(logo)
    score = 0
    game_on = True
    a = get_person()
    while game_on:
        b = get_person()
        print_info(a, b)
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        print(5*"\n")
        if check_answer(answer, a, b):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_on = False
            print(f"Sorry, that's wrong. Final score: {score}")
        a = b


start_game()