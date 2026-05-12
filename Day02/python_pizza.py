print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0
# todo: work out how much they need to pay based on their size choice.
if size.lower() == "s":
    total += 15
elif size.lower() == "m":
    total += 20
elif size.lower() == "l":
    total += 25
# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni.lower() == "y":
    if size.lower() == "s":
        total += 2
    else:
        total += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese.lower() == "y":
    total += 1

print(f"Your total: ${total}")

# Based on a user's order, work out their final bill. Use the
# input () function to get a user's preferences and then add up
# the total for their order and tell them how much they have to pay.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
# Example Interaction
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza?
# Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.