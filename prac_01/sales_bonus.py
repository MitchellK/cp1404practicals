"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
base_bonus = 0

while sales >= 0:
    if sales < 1000:
        base_bonus = 0.1
    elif sales >= 1000:
        base_bonus = 0.15
    actual_bonus = sales * base_bonus
    print(actual_bonus)
    sales = float(input("Enter sales: $"))
print("uh oh! that was negative!")


