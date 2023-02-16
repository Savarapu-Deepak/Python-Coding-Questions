# Python Program to check the given number is prime or not.

num = int(input('Enter Any Number : '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, ' is not a Prime NUmber')
            break
    else:
        print(num, 'is a Prime Number')