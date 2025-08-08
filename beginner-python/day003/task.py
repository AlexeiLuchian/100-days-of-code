print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("You got to a crossroad, are you going left or right? right / left: ")
if left_or_right == "left":
    print("You chose the right path.")
    swim_or_wait = input("You arrived at a lake. Are you waiting or are you swimming to the other shore? swim / wait: ")
    if swim_or_wait == "wait":
        print("The lake has dried up and three doors appear in sight.")
        door = input("Which door are you opening? blue / yellow / red : ")
        if door == "yellow":
            print("You arrived in Romania, you win!")
        elif door == "red":
            print("I don't know where you arrived but you lost.\nGame Over!")
        elif door == "blue":
            print("I don't know how but you're in Finland and you froze.\nGame Over!")
        else:
            print("Surprise!\nGame Over!")
    else:
        print("You were attacked by a trout.\nGame Over!")
else:
    print("You fell into a hole.\nGame Over!")
