"""CP1404/CP5632 Practical - Programming Language Intermediate Exercise"""

from prac_06.programming_language import ProgrammingLanguage

# Languages entered
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# test print of Python using __str__
print(python.__str__())

# create list of languages
list_of_languages = [ruby, python, visual_basic]

# print a list of the dynamically typed languages
print("The dynamically typed languages are:")
for language in list_of_languages:
    if language.is_dynamic():
        print(language.name)

