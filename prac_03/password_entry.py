"""
Mitchell
"""


def main():
    user_password = get_password()
    display_pass(user_password)


def get_password():
    new_pass = ""
    while len(new_pass) < 6:
        new_pass = input("Please enter a new password that is at least 6 characters in length")
    return new_pass


def display_pass(password):
    for i in range(0, len(password)):
        print('*', end="")


main()
