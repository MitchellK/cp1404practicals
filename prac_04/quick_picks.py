"""
Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.
- Each line (quick pick) should not contain any repeated number.
- Each line of numbers should be displayed in sorted (ascending) order.
"""

import random

# Set the range of values that are able to be selected for an individual pick
LOWEST_PICK_NUMBER = 1
HIGHEST_PICK_NUMBER = 45
NUMBERS_PER_PICK = 6


# get number_of_picks from the user, for that many times, generate a quick pick and print it.
# No repeats, printed ascending order.
def main():
    number_of_picks = get_number_of_picks()
    for i in range(number_of_picks):
        quick_pick = generate_picks()
        display_picks(quick_pick)


# get number of picks and return them, along with error checking.
def get_number_of_picks():
    number = input("Please enter the number of quick picks you require: ")
    while number.isalpha():
        print("Invalid Choice!")
        number = input("Please enter the number of quick picks you require: ")
    number = int(number)
    return number


# generates 6 picks from the globally set ranges and returns as a list, no repeating numbers
def generate_picks():
    new_pick = []
    for i in range(NUMBERS_PER_PICK):
        number = random.randint(LOWEST_PICK_NUMBER, HIGHEST_PICK_NUMBER)
        while number in new_pick:
            number = random.randint(LOWEST_PICK_NUMBER, HIGHEST_PICK_NUMBER)
        new_pick.append(number)
    return new_pick


# sorts the picks and then displays the picks lowest to highest
def display_picks(pick):
    pick.sort()
    print(" ".join("{:2}".format(number) for number in pick))


main()
