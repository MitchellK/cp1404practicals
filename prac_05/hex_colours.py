"""
CP1404 Practical instructions:
Create a program that allows you to:
- Look up hexadecimal colour codes like those at http://www.color-hex.com/color-names.html
- Use a constant dictionary of about 10 colour names
- User to enter a name and get the code, e.g. entering AliceBlue should show #f0f8ff.
- Entering an invalid colour name should not crash.
- Allow the user to enter names until they enter a blank one to stop the loop
"""

COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000",
           "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "burlywood": "#deb887",
           "CadetBlue": "#5f9ea0", "chocolate": "#d2691e", "CornflowerBlue": "#6495ed"}

print("The available colours are:")
for entry in COLOURS:
    print(entry)

user_selection = input("Please type the name of a colour to return it's code:")
while user_selection != "":
    if user_selection in COLOURS:
        print("The code for {} is: {}".format(user_selection, COLOURS[user_selection]))
    else:
        print("Invalid selection, choose from available colours \nnote: case is sensitive")
    user_selection = input("Please type the name of a colour to return it's code:")
