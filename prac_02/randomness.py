import random

for i in range(3):
    print("randint:", random.randint(5, 20))  # line 1
    print("randrange:", random.randrange(3, 10, 2))  # line 2
    print("uniform:", random.uniform(2.5, 5.5))  # line 3

"""
What was seen on Line 1? what was the smallest and largest numbers possible?
    - 16, 16, 19
    - smallest number is 5, largest number is 20

What was seen on Line 2? what was the smallest and largest numbers possible? Could a 4 be produced?
    - 3, 3, 9 ##what are the odds of the double 16 and then a double 3!!
    - smallest number is 3, largest is 9
    - 4 is not possible, as the increment is 2 starting at 3.

What was seen on Line 3? what was the smallest and largest numbers possible?
    - 2.804044814242501, 2.7649386824404405, 3.7969253117442205
    - the smallest number is 2.5 and the largest is 5.5


#####Sample Output#####
randint: 16
randrange: 3
uniform: 2.804044814242501
randint: 16
randrange: 3
uniform: 2.7649386824404405
randint: 19
randrange: 9
uniform: 3.7969253117442205
"""

