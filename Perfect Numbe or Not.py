# Python Program to print number is Perfect or not

num = int(input('Enter Any NUmber : '))
check = num
sum = 0
if num > 0:
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    else:
        if check == sum:
            print(num, ' is a Perfect Number')
        else:
            print(num, ' is not a Perfect Number')
else:
    print('Number Should be greater than 0')