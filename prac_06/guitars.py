"""CP1404/CP5632 Practical - Programming Language Do From Scratch Exercise

The program should use a list to store all of the user's guitars
- (keep inputting until they enter a blank name)
then print their details.
"""

from prac_06.guitar_class import Guitar


def main():
    list_of_user_guitars = []
    ''' Test data
    list_of_user_guitars.append(Guitar("new", 2018, 999))
    list_of_user_guitars.append(Guitar("vintage", 1900, 99999999999))
    list_of_user_guitars.append(Guitar("outlier testing for things", 1000, 2))
    '''
    print("Welcome to GUITARS! Please enter your Guitars and information here:")
    guitar_name = " "
    while guitar_name != "":
        guitar_name = input("Name: ")
        if guitar_name != "":
            guitar_year = int(input("Year: "))
            guitar_cost = float(input("Cost: "))
            list_of_user_guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))

    # determines longest guitar length and longest cost
    longest_guitar_name_length = max(len(i.name) for i in list_of_user_guitars)

    # TODO: fix this and add to filter
    # longest cost doesnt work, as it needs a variable number based on the largest.
    #longest_guitar_cost_length = max(len(str(i.cost)) for i in list_of_user_guitars)
    #print(longest_guitar_cost_length)

    print("These are my guitars:")
    for count, guitar in enumerate(list_of_user_guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() == True else ""
        print("Guitar {}: {:{}} ({}), worth ${:,.2f} {:}".format(count, guitar.name, longest_guitar_name_length,
                                                                 guitar.year, guitar.cost, vintage_string))


main()
