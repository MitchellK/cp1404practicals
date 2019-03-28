"""
CP1404 - Practical
Write a program to:
- Count the occurrences of words in a string.
- Ask the user for a string
- Print the counts of how many of each word are in the file
- After you have the program working, make your program do this sorting
- Align the numbers so they are in one nice column (see prac for notes)
"""


def main():
    # Prompt for text
    phrase = input("enter a phrase:")
    new_dictionary = convert_to_dict(phrase)
    longest_word = get_longest_word(new_dictionary)

    # TODO: need to improve sorting. should use tuples of dict instead
    # add in sort by key
    sort_list = []
    for key in new_dictionary:
        sort_list.append(key)
    sort_list.sort()

    # sort by amount
    second_sort_list = []
    for k in new_dictionary.values():
        if k not in second_sort_list:
            second_sort_list.append(k)
    second_sort_list.sort(reverse=True)

    # print the dictionary (each word and count)
    # hint: print("{:{}} = {}".format(x, y, z))
    print("Below is the dictionary sorted by key:")
    for i in sort_list:
        print("{:{}}: {}".format(i, longest_word, new_dictionary[i]))

    print("\n\nBelow is the dictionary sorted by value")
    for n in second_sort_list:
        for ke, val in new_dictionary.items():
            if n == val:
                print("{:{}}: {}".format(ke, longest_word, val))


def convert_to_dict(string):
    # place each word into a dictionary with a count of 1, check if it exists, if so add a count
    dictionary = {}
    for each in string.split():
        try:
            dictionary[each] += 1
        except KeyError:
            dictionary[each] = 1
    return dictionary


def get_longest_word(dictionary):
    # align them to a column(use a variable that calculates the longest word)
    length = 0
    for word in dictionary:
        if len(word) > length:
            length = int(len(word))
    return length


main()
