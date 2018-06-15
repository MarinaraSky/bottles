#!/usr/bin/env python3

import random
import sys
# make a module to put here, will be used for user input verification


def sing(bottles):
    """This function will take an integer and sing however many bottles of
    of beverage needed until there are no more bottles on the wall"""

    # The lyrics to the songs with format string syntax
    firstLine = "{} bottles of beer on the wall!"
    secondLine = "{} bottles of beer!"
    passIt = "Take one down \nAnd Pass it around"
    if bottles == 1:    # Checking to see if last bottle on wall
        print(firstLine.format(bottles).replace("bottles", "bottle"))
        print(secondLine.format(bottles).replace("bottles", "bottle"))
        print(passIt)
        print("No more bottles of beer on the wall!")
    elif bottles > 1:
        print(firstLine.format(bottles))
        print(secondLine.format(bottles))
        print(passIt)
        bottles -= 1        # This is to print 1 less bottle for the last line
        if bottles == 1:
            print(firstLine.format(bottles).replace("bottles", "bottle"))
        else:
            print(firstLine.format(bottles))
    else:
        pass
    print()


def main():
    """Main will loop through the sing function 98 times and sing bottles of
    beer on the wall"""
    if sys.argv[1] == "":
        try:
            choice = input("Enter y to start with a random "
                           "number(ENTER for 99): ")
        except (KeyboardInterrupt, EOFError):
            print()
            return 2
        if choice.lower() == "y":
            wall = random.randint(1, 99)
        elif (choice == "") or (choice.lower() == "n"):
            wall = 99
        else:
            print("INVALID CHOICE")
            return 1
    elif int(sys.argv[1]) >= 1:
        wall = int(sys.argv[1])
    while wall >= 1:     # Loop to decrement number passed to the song
        sing(wall)
        wall -= 1


if __name__ == "__main__":
    main()
