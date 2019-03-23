"""
BASIC LIST OPERATIONS
The program should then output various interesting things.
"""


# Runs functions
def main():
    numbers = get_numbers()
    display_various(numbers)


# Prompts users for numbers and adds them to a list, returns list.
def get_numbers():
    numbers_to_get = 5
    user_numbers = []
    print("Please enter {} numbers to be stored\n".format(numbers_to_get))
    for i in range(1, numbers_to_get + 1):
        user_numbers.append(int(input("Please enter number {}: ".format(i))))
    return user_numbers


# displays various data about the number list that is imported
def display_various(current_numbers):
    for entry in current_numbers:
        print("Number: {}".format(entry))
    print("The first number is {}".format(current_numbers[0]))
    print("The last number is {}".format(current_numbers[-1]))
    print("The smallest number is {}".format(min(current_numbers)))
    print("The largest number is {}".format(max(current_numbers)))
    print("The average of the numbers is {}".format(sum(current_numbers) / len(current_numbers)))


main()
