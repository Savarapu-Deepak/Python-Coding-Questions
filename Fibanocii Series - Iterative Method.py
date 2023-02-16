# Python Program to print Fibonocii Series using Iterative Method.

num = int(input('Enter Range of the Fibonocii Series : '))
n1, n2 = 0, 1
for i in range(num + 1):
    print(n1)
    next_NUmber = n1 + n2
    n1 = n2
    n2 = next_NUmber
