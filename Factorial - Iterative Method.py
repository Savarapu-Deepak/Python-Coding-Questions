# Python Program to print Factorial of a number using Iterative Method

num = int(input('Enter Number : '))
fact = 1
if num < 0:
    print('Number Should be Greater than or equal to 1')
elif num == 0:
    print('Factorial of 1 is 1')
else:
    for i in range(1, num + 1):
        fact = fact * i
    else:
        print('Factorial of the given number {} is {}'.format(num, fact))

