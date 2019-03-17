# print odd numbers from 1-20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# print 0 - 100 in 10's
for i in range(0, 100, 10):
    print(i, end=' ')
print()

# print number of stars requested
number_of_stars = int(input("How many stars would you like to print?"))
for i in range(0, number_of_stars):
    print('*', end=' ')
print()

# as above but cumulative prints on new lines
number_of_stars = int(input("How many stars would you like to print?"))
for i in range(0, number_of_stars):
    for x in range(i+1):
        print('*', end=' ')
    print()
print()
