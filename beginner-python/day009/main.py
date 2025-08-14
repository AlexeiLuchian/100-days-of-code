from art import logo

print(logo)

user_name = input("What is your name?: ")
user_bid = float(input("What is you bid?: $"))

bidders = {user_name: user_bid}

more_bidders = input("Are there any other bidders? type 'yes' or 'no': ").lower()

while more_bidders == "yes":
        user_name = input("What is your name?: ")
        user_bid = float(input("What is you bid?: $"))
        bidders[user_name] = user_bid

        more_bidders = input("Are there any other bidders? type 'yes' or 'no': ").lower()
        if more_bidders != "yes":
            more_bidders = False

biggest_bid = 0
winner = ""
for name in bidders:
    if bidders[name] > biggest_bid:
        biggest_bid = bidders[name]
        winner = name

print(f"The winner is {winner} with a bid of ${biggest_bid}")