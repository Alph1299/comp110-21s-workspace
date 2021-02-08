"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730279779"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune: int = int(randint(1, 4))

if fortune == 1:
    print("You will encounter great fortune.")
else: 
    if fortune == 2:
        print("Your family will prosper.")
    else: 
        if fortune == 3:
            print("A loved one will flourish.")
        else:
            if fortune == 4:
                print("The sun will be bright for you.") 
print("Now, go spread positive vibes!")