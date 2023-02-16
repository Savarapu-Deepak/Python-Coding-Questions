# Python Program to reverse a number.

num = int(input("Enter Any NUmber : "))
check = num
reverse = 0
while num > 0:
    rem = num % 10
    reverse = (reverse * 10) + rem
    num //= 10
else:
    print('Reverse of the number {} is {}'.format(check, reverse))
