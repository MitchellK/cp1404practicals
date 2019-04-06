"""CP1404/CP5632 Practical - Programming Language Intermediate Exercise"""

class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

