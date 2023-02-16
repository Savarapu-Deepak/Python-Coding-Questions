# Check given number representation is Binary or not.

num = int(input('Enter Any Number : '))
check = num
while num > 0:
    if num % 10 != 0 and num % 10 != 1:
        print(num, 'Not a Binary Number')
        break
    else:
        num = num // 10
    if num == 0:
        print(check, 'is Binary Number')