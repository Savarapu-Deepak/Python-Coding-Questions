# Python Program to Swap two numbers without using third variable.

x = int(input('Enter x Value : '))
y = int(input('Enter y value : '))
print("Before Swap : ", x, y)
# By Tuple Un-Packing
x, y = y, x
print('After Swap : ',x, y)