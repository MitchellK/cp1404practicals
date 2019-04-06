"""CP1404/CP5632 Practical - Programming Language Do From Scratch Exercise
program to test guitar class
"""

from prac_06.guitar_class import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
ibanez = Guitar("Ibanez S6570SK Prestige", 2005, 2799.00)

list_of_guitars = [gibson, ibanez]

for guitar in list_of_guitars:
    print(guitar.__str__())

print("...Testing Class Methods...")
print("{} get_age() - Expected 96 got {}".format(gibson.name, gibson.get_age()))
print("{} is_vintage() - Expected True got {}".format(gibson.name, gibson.is_vintage()))
print("{} get_age() - Expected 13 got {}".format(ibanez.name, ibanez.get_age()))
print("{} is_vintage() - Expected False got {}".format(ibanez.name, ibanez.is_vintage()))

