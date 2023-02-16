# Python Program to print GCD or HCF using Recursion....

def HCF_or_GCD(a, b):
    assert a >= 0 and int(a) ==a and b >= 0 and int(b) == b, 'Positive Integers only'
    if b > a:
         a, b = b, a
    elif b == 0:
        return a
    else:
        return HCF_or_GCD(b, a % b)
a = int(input('Enter a Value : '))
b = int(input('Enter b Value : '))
res = HCF_or_GCD(a, b)
print(res)