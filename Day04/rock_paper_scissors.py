import random
import sys

def main():
    while True:
        print("Would you like to play Rock-Paper-Scissors? \"Y\"es or \"N\"o?")
        to_play = input("  > ").lower()
        if to_play == "y":
            break
        elif to_play == "n":
            sys.exit("\nSorry we didn't get the chance to play. Maybe next time!")
        else:
            print("\"" + to_play + "\" is not a valid entry. Try again.\n")
            continue

    while True:
        print()

        while True:
            print("Enter \"1\" for Rock, \"2\" for Paper, or \"3\" for Scissors")
            user_selection = input("  > ").lower()
            if user_selection == "1" or user_selection == "2" or user_selection == "3":
                user_selection = int(user_selection)
                break
            else:
                print("\"" + user_selection + "\" is not a valid entry. Try again.\n")
                continue

        comp_selection = random.randint(1, 3)

        print()

        if user_selection == comp_selection:
            print("It is a tie!")
        elif user_selection == 1 and comp_selection == 3:
            print("You win!")
        elif user_selection == 2 and comp_selection == 1:
            print("You win!")
        elif user_selection == 3 and comp_selection == 2:
            print("You win!")
        else:
            print("You lost...")

        print()

        while True:
            print("Would you like to play again? \"Y\"es or \"N\"o?")
            exit_input = input("  > ").lower()
            if exit_input == "y":
                break
            elif exit_input == "n":
                sys.exit("\nThanks for playing!")
            else:
                print("\"" + exit_input + "\" is not a valid entry. Try again.\n")
                continue

        continue
                

if __name__ == "__main__":
    main()
