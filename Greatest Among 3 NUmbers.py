# Write a program in Python to find greatest among three integers.

x = int(input('Enter Number_1 : '))
y = int(input('Enter Number_2 : '))
z = int(input('ENter Number_3 : '))

if x > y and x > z:
    print(x, 'is greater than ', y, ' and', z)
elif y > z:
    print(y, 'is greater than ', z, ' and', x)
else:
    print(z, 'is greater than ', x, ' and', y)