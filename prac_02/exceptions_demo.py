"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - When a numerator or denominator that is not a number is entered. Such as an 'A' or an '!'
2. When will a ZeroDivisionError occur?
    - when you enter the denominator as 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - adding a while loop to warn and ask the user for a valid number
    - we could do the same for numerator
    - we could also offer the user an end choice within the while loop if they don't want to continue
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        denominator = int(input("Dividing by zero is dangerous!! Please enter any other number"))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")