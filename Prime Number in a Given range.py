# Python Program to print prime number in a given range

lower = int(input('Enter Lower Value : '))
upper = int(input('Enter Upper Value : '))
for i in range(lower, upper):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, 'is a Prime Number')