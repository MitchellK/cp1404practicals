"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    user_score = float(input("Enter score: "))
    determined_status(user_score)


def determined_status(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
