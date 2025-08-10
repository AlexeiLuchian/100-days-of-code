import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    print("Invalid choice!")
else:
    if user_choice == computer_choice:
        print("You chose:")
        print(images[user_choice])
        print("Computer chose:")
        print(images[computer_choice])
        print("It's a draw!")
    elif user_choice > computer_choice and user_choice - computer_choice == 1 or user_choice == 0 and computer_choice == 2:
        print("You chose:")
        print(images[user_choice])
        print("Computer chose:")
        print(images[computer_choice])
        print("You win!")
    else:
        print("You chose:")
        print(images[user_choice])
        print("Computer chose:")
        print(images[computer_choice])
        print("You lose!")