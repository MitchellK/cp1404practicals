"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


# Displays menu, passes result into the relevant converter, then into a display function.
def main():
    user_choice = display_menu()
    while user_choice != "Q":
        if user_choice == "C":
            converted_temp = convert_fahrenheit()
        elif choice == "F":
            converted_temp = convert_celcius()
        else:
            print("Invalid option")
        display_converted_temp(converted_temp)
        user_choice = display_menu()
    print("Thank you.")


def display_menu():
    global MENU, choice
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    return choice


def convert_celcius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    temp = "Result: {:.2f} C".format(celsius)
    return temp


def convert_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    temp = "Result: {:.2f} F".format(fahrenheit)
    return temp


def display_converted_temp(result):
    print(result)


main()
