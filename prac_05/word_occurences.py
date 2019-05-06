"""
Name: Mitchell Kelleher
CP1404 - Practical
Write a program to count the occurrences of words in a string with the below requirements:
- Ask the user for a string
- Print the counts of how many of each word are in the file
- Sort the output (key or value?)
- Align the numbers so they are in one nice column (see prac for notes)
"""

from operator import itemgetter


def main():
    # requests phrase from user
    phrase = input("enter a phrase:")
    dictionary_of_phrase = convert_phrase_to_dict(phrase)
    longest_word = get_longest_word_length(dictionary_of_phrase)
    phrase_as_list = initialize_sorting_list(dictionary_of_phrase)

    for i in phrase_as_list:
        print("{i}".join(" ", end=""))

    # Sorting the list by key and then printing
    phrase_as_list.sort()
    print("Below is the dictionary sorted by key:")
    for i in phrase_as_list:
        print("{:{}}: {}".format(i[0], longest_word, i[1]))

    # sorting the list by value and then printing
    phrase_as_list.sort(key=itemgetter(1), reverse=True)
    print("Below is the dictionary sorted by value:")
    for i in phrase_as_list:
        print("{:{}}: {}".format(i[0], longest_word, i[1]))


# converts the user's string to a dictionary
def convert_phrase_to_dict(string):
    # place each word into a dictionary with a count of 1, check if it exists, if so add a count
    dictionary = {}
    for each in string.split():
        try:
            dictionary[each] += 1
        except KeyError:
            dictionary[each] = 1
    return dictionary


# determines the longest word in the dictionary, used for printing the output
def get_longest_word_length(dictionary):
    length = 0
    for word in dictionary:
        if len(word) > length:
            length = int(len(word))
    return length


# creates a list from the new_dictionary to use the sort method
def initialize_sorting_list(dictionary):
    sort_list = []
    for key, value in dictionary.items():
        sort_list.append([key, int(value)])
    return sort_list


main()
