# Python Program to add two numbers without using a arithmatic operator

x = int(input('Enter x value : '))
y = int(input('ENter y Value : '))

res = int.__add__(x, y)
print('Addition of {} and {} is {}'.format(x, y, res))