"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


# displays MENU, get's user choice, determines relevant converter, then into a display function.
def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            temp = float(input("Fahrenheit: "))
            converted_temp = convert_fahrenheit(temp)
            print("Result: {:.2f} C".format(converted_temp))
        elif choice == "F":
            temp = float(input("Celsius: "))
            converted_temp = convert_celcius(temp)
            print("Result: {:.2f} F".format(converted_temp))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celcius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
