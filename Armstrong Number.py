# Python Program to check given number is armstrong or not

num = int(input('Enter Any Number : '))
check = num
sum = 0
y = len(str(num))
while num > 0:
    rem = num % 10
    sum = sum + (rem ** y)
    num //= 10
else:
    if check == sum:
        print(sum, 'is an Armstrong NUmber')
    else:
        print(sum, 'is not an Armstrong Number')
