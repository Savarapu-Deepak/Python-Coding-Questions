# Python Program to print Prime Numbers upto n.

num = int(input('Enter LAst Value : '))
for i in range(1, num + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
             break
        else:
            print(i, 'is a Prime Number')