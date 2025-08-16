from art import logo
from random import randint

def get_user_cards():
    return [randint(2,12),randint(2,12)]

def get_card():
    return randint(2,12)

def show_cards(user_cards, bot_card):
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {bot_card}")

def show_final_cards(user_cards, bot_cards):
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's final cards: {bot_cards}")

def check_valid_score(cards):
    if sum(cards) > 21:
        for i in range(len(cards)):
            if cards[i] == 11:
                cards[i] = 1
    if sum(cards) > 21:
        return False
    return True

def get_bot_cards(card):
    bot_cards = [card]
    while sum(bot_cards) < 17:
        bot_cards.append(get_card())
    return bot_cards

def get_winner(user_cards, bot_card):
    if sum(user_cards) > 21:
        print("You LOST")
        show_final_cards(user_cards, bot_card)
    else:
        bot_cards = get_bot_cards(bot_card)
        if sum(bot_cards) > 21:
            print("You WON")
        else:
            if sum(user_cards) > sum(bot_cards):
                print("You WON")
            elif sum(bot_cards) == sum(user_cards):
                print("It's a TIE!")
            else:
                print("You LOST")
        show_final_cards(user_cards,bot_cards)

    start_game()


def blackjack():
    print("\n"*20)
    print(logo)
    user_cards = get_user_cards()
    bot_card = get_card()
    show_cards(user_cards,bot_card)
    choice = input("Type 'y' to get another card, tpe 'n' to pass: ")
    while choice == 'y':
        user_cards.append(get_card())
        if not check_valid_score(user_cards):
            break
        show_cards(user_cards, bot_card)
        choice = input("Type 'y' to get another card, tpe 'n' to pass: ")
    get_winner(user_cards,bot_card)


def start_game():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice == "y":
        blackjack()
    else:
        print("ok bye")

start_game()