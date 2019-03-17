""""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, a 10% discount is applied to that total before the amount is displayed on the screen.
"""

total_cost = 0
OVER_100_DISCOUNT = 0.1
number_of_items = int(input("How many items do you have?"))

# error check for negative numbers
while number_of_items < 0:
    number_of_items = int(input("Invalid number of items! please enter a positive number"))

# get cost of each item, TO DO: to itemise a receipt use a list
for i in range(0, number_of_items):
    total_cost += float(input("Please enter the price of an item"))

# print total cost apply discount if over $100
if total_cost <= 100:
    print("The total price for", number_of_items, "items is $", total_cost)
else:
    discount = total_cost * OVER_100_DISCOUNT
    total_cost = total_cost - discount
    print("The total price for", number_of_items, "items is $", total_cost)
