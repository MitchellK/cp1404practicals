"""
Run this program, it will explain each question and what i've done :)
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

print("""This is the written test. The questions are printed, and my answer is underneath.
The list we are using is numbers = {}\n""".format(numbers))

print("1. numbers[0] is {}".format(numbers[0]))
print("i answered 3\n")
print("2. numbers[-1] is {}".format(numbers[-1]))
print("i answered 2, though it did take some deliberation considering question 4. But it helped me learn :)\n")
print("3. numbers[3] is {}".format(numbers[3]))
print("i answered 1\n")
print("4. numbers[:-1] is {}".format(numbers[:-1]))
print("I said this code prints list to one before the end, printing to the end would be [x:]\n")
print("5. numbers[3:4] is {}".format(numbers[3:4]))
print("i answered 1\n")
print("6. 5 in numbers is:", 5 in numbers)
print("i answered TRUE\n")
print("7. 7 in numbers is:", 7 in numbers)
print("i answered FALSE\n")
print("8. \"3\" in numbers is:", "3" in numbers)
print("i answered FALSE\n")
print("9. numbers + [6,5,3] will add these numbers to the list.... See ->", numbers + [6,5,3])
print("i answered that this would add to the list\n")

print("More Numbers work! remember the list is currently numbers = {}\n".format(numbers))

print("1. change the first element of numbers to \"ten\"")
numbers[0] = "ten"
print("I used: numbers[0] = \"ten\"\n")

print("change the last element of numbers to 1")
numbers[-1] = 1
print("I used: numbers[-1] = 1\n")

print("get all the elements from numbers except the first two")
print("I used numbers[2:] to print {}\n".format(numbers[2:]))

print("check if 9 is an element of numbers")
print("I used 9 in numbers to check this and it was {}\n".format(9 in numbers))

print("And just to check, numbers is now: \n numbers = {}".format(numbers))
