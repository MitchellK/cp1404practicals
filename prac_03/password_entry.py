"""
Mitchell
"""

MIN_LENGTH = 6


def main():
    user_password = password_entry()
    display_pass(user_password)


def password_entry():
    new_pass = ""
    while len(new_pass) < MIN_LENGTH:
        new_pass = input("Please enter a new password that is at least {} characters in length".format(MIN_LENGTH))
    return new_pass


def display_pass(password):
    for i in range(0, len(password)):
        print('*', end="")


main()

