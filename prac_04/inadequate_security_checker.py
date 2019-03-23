"""
Ask the user for their username. If the username is in the above list of authorised users, print "Access granted",otherwise print "Access denied"
"""

# authorised list of users
USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


# main calls functions and sets variables to be passed
def main():
    username = get_username()
    authorised = check_username(username)
    display_access_result(authorised)


# prompt user for login and return
def get_username():
    user_login = input("Please enter your username:")
    return user_login


# parse login details to be checked against authorised logins
def check_username(login):
    if login in USERNAMES:
        return True
    else:
        return False


# Displays Access Granted or Denied based on checker
def display_access_result(result):
    if result:
        print("Access Granted")
    else:
        print("Access Denied")


main()
