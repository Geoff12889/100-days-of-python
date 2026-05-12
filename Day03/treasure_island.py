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

print("You are at a crossroads. Do you go \"left\" or \"right\"?")
choice1 = input("Enter \"left\" or \"right\"\n> ").lower()

if choice1 == "right":
    print("You come to a river. Do you \"swim\" or take a \"boat\"?")
    choice2 = input("Enter \"swim\" or \"boat\"\n> ").lower()

    if choice2 == "boat":
        print("You arrive at a house. There are three "
              "door. Do you entere the \"red\", \"yellow\", "
              "or \"blue\" door?")
        choice3 = input("Enter \"red\", \"yellow\", or \"blue\"\n> ").lower()

        if choice3 == "yellow":
            print("You entered a room full of treasure. You win!!")
        elif choice3 == "red":
            print("You entered a burning room. Game over")
        elif choice3 == "blue":
            print("You entered a flooded room and drowned. Game over")
        else:
            print("Game over")

    else:
        print("You attempt to swim but drown. Game over")
else:
    print("A coyote attacks you. Game over")