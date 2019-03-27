"""
CP1404 - Practical
Write a program to:
- count the occurrences of words in a string.
- Ask the user for a string
- print the counts of how many of each word are in the file
- After you have the program working, make your program do this sorting
- align the numbers so they are in one nice column (see prac for notes)
"""

# Prompt for text
string = input("enter a phrase:")
# place each word into a dictionary with a count of 1, check if it exists, if so add a count
new_list = []
for each in string:
    new_list.append(each)
print(new_list)

# print the dictionary (each word and count)
# add in sort and align them to a column(use a variable that calculates the longest word)
# hint: print("{:{}} = {}".format(x, y, z))

