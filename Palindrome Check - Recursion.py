# Palindrome check using Recursion.

def Palindrome(n, t):
    assert n >= 0 and int(n) == n, 'Positive Integer Only'
    if n == 0:
        return t
    else:
        t = (t * 10) + (n % 10)
        return Palindrome(n // 10, t)
num = int(input('Enter Any Number : '))
temp = 0
res = Palindrome(num, temp)
if num == res:
    print(res, 'is a Palindrome')
else:
    print(res, 'is not a Palindrome')
