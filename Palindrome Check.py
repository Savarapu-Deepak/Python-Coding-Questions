# Python Program to check given number is Palindrome or not.

'''num = int(input('Enter Any Number : '))
check = num
rev = 0
while num > 0:
    rem = num % 10
    rev = (rev * 10) + rem
    num //= 10
else:
    if check == rev:
        print(rev, 'is a Palindrome Number')
    else:
        print(rev, 'is not a Palindrome')'''

x = [1, 2, 3, 2, 3, 3, 2, 2, 5]
z = []
count = 0
for y in x:
    res = x.count(y)
    if res > count:
        count = res
        num = y
else:
    print(num)



















