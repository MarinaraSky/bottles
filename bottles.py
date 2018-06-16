#!/usr/bin/env python3

import random
import sys
import time


TEENS = {"19": "Nineteen", "18": "Eighteen", "17": "Seventeen",
         "16": "Sixteen", "15": "Fifteen", "14": "Fourteen",
         "13": "Thirteen", "12": "Twelve", "11": "Eleven"}

TENSPLACE = {"9": "Ninety", "8": "Eighty", "7": "Seventy", "6": "Sixty",
             "5": "Fifty", "4": "Forty", "3": "Thirty", "2": "Twenty",
             "1": "Ten"}

ONEPLACE = {"9": "Nine", "8": "Eight", "7": "Seven", "6": "Six", "5": "Five",
            "4": "Four", "3": "Three", "2": "Two", "1": "One", "0": ""}


def numToWord(bottles, beverage):
    """This function will translate the number of bottle in digits
    to words. Will return a tuple used for format string of song"""
    bottlesStr = str(bottles)
    if len(bottlesStr) == 2:    # Checking if double digits
        if bottles < 20 and bottles > 10:   # Checking if number is in teens
            wordNum = TEENS[bottlesStr]
            printFormat = (wordNum, beverage)
        else:
            wordNum = TENSPLACE[bottlesStr[0]] + "-" +\
                  ONEPLACE[bottlesStr[1]].lower()
        if bottles % 10 == 0:   # Checking if its a mutliple of 10
            wordNum = wordNum.replace("-", "")
        printFormat = (wordNum, beverage)
    else:   # If bottles is single digit
        printFormat = (ONEPLACE[bottlesStr[0]], beverage)
    return printFormat


def sing(bottles, beverage):
    """This function will take an integer and sing however many bottles of
    of beverage needed until there are no more bottles on the wall"""
    # The lyrics to the songs with format string syntax
    firstLine = "{} bottles of {} on the wall!"
    secondLine = "{} bottles of {}!"
    passIt = "Take one down\nAnd pass it around"
    formatTup = numToWord(bottles, beverage)
    if bottles == 1:    # Checking to see if last bottle on wall
        print(firstLine.format(*formatTup).replace("bottles", "bottle"))
        print(secondLine.format(*formatTup).replace("bottles", "bottle"))
        print(passIt)
        print("No more bottles of {} on the wall!".format(beverage))
    elif bottles > 1:   # When not last bottle on wall
        print(firstLine.format(*formatTup))
        print(secondLine.format(*formatTup))
        print(passIt)
        bottles -= 1        # This is to print 1 less bottle for the last line
        formatTup = numToWord(bottles, beverage)
        if bottles == 1:
            print(firstLine.format(*formatTup).replace("bottles", "bottle"))
        else:
            print(firstLine.format(*formatTup))
    else:
        pass
    print()


def main():
    startTime = time.time()
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
    elif int(sys.argv[1]) < 1:
        return print("INVALID NUMBER")
    elif int(sys.argv[1]) >= 1:
        wall = int(sys.argv[1])
        beverage = sys.argv[2]
    while wall >= 1:     # Loop to decrement number passed to the song
        sing(wall, beverage)
        wall -= 1
    endTime = time.time()
    runTime = endTime - startTime
    print("It took {} seconds to sing Bottles to you. ".format(runTime))


if __name__ == "__main__":
    main()
