import random

NAMES = "name.txt"
## Create name.txt to store a prompted name
file_name = open(NAMES, 'w')
user_name = input("Hello there! What is your name? ")
print(user_name, file=file_name)
file_name.close()

## Open name.txt to import the name and display it
which_name = open(NAMES, 'r')
current_name = which_name.read().strip()
print("Hi there", current_name + ", I hope you are doing well!")
which_name.close()

## Open existing file numbers and add them!
NUMBERS = "numbers.txt"
current_numbers = open(NUMBERS, "r")
number_1 = int(current_numbers.readline())
number_2 = int(current_numbers.readline())
sum_of_numbers = number_1 + number_2
print(sum_of_numbers)
current_numbers.close()

## generating list of numbers to be used below
gen_numbers = open("unlimited_numbers.txt", "w")
for i in range(1, random.randint(2, 1000)):
    print(random.randint(1, 999), file=gen_numbers)
gen_numbers.close()

#Printing the sum of an endless list of numbers
UNLIMITED_NUMBERS = "unlimited_numbers.txt"
current_numbers = open(UNLIMITED_NUMBERS, "r")
sum_of_numbers = 0
for i in current_numbers:
    new_number = int(i)
    sum_of_numbers += new_number
print(sum_of_numbers)
current_numbers.close()
