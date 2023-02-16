# Python Program to check given number is Palindrome or not.

num = int(input('Enter Any Number : '))
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
        print(rev, 'is not a Palindrome')
