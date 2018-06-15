#!/usr/bin/env python3

import random
import sys
# make a module to put here, will be used for user input verification


def sing(bottles, beverage):
    """This function will take an integer and sing however many bottles of
    of beverage needed until there are no more bottles on the wall"""

    # The lyrics to the songs with format string syntax
    firstLine = "{} bottles of {} on the wall!"
    secondLine = "{} bottles of {}!"
    passIt = "Take one down \nAnd Pass it around"
    formatTup = (bottles, beverage)
    if bottles == 1:    # Checking to see if last bottle on wall
        print(firstLine.format(*formatTup).replace("bottles", "bottle"))
        print(secondLine.format(*formatTup).replace("bottles", "bottle"))
        print(passIt)
        print("No more bottles of {} on the wall!".format(beverage))
    elif bottles > 1:
        print(firstLine.format(*formatTup))
        print(secondLine.format(*formatTup))
        print(passIt)
        bottles -= 1        # This is to print 1 less bottle for the last line
        formatTup = (bottles, beverage)
        if bottles == 1:
            print(firstLine.format(*formatTup).replace("bottles", "bottle"))
        else:
            print(firstLine.format(*formatTup))
    else:
        pass
    print()


def main():
    """Main will loop through the sing function 98 times and sing bottles of
    beer on the wall"""
    beverage = "beer"
    if len(sys.argv) == 1:      # Arguments are checked for validity
        try:
            choice = input("Enter y to start with a random "
                           "number(ENTER for 99): ")
        except (KeyboardInterrupt, EOFError):
            return print()
        if choice.lower() == "y":
            wall = random.randint(1, 99)
        elif (choice == "") or (choice.lower() == "n"):
            wall = 99
        else:
            return print("INVALID CHOICE")
    elif len(sys.argv) > 3:
        return print("TOO MANY ARGUMENTS")
    elif len(sys.argv) == 2:
        return print("NOT ENOUGH ARGUMENTS")
    elif sys.argv[1].isnumeric() is False or int(sys.argv[1]) > 99:
        return print("INVALID NUMBER")
    elif int(sys.argv[1]) >= 1:
        wall = int(sys.argv[1])
        beverage = sys.argv[2]
    while wall >= 1:     # Loop to decrement number passed to the song
        sing(wall, beverage)
        wall -= 1


if __name__ == "__main__":
    main()
