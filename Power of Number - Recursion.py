# Python Program to print Power of a number using Recursion.

def Power(base, exp):
    assert int(exp) == exp , 'Exponential Integer only Accepted'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / base * Power(base, exp + 1)
    else:
        return base * Power(base, exp - 1)

base = int(input('Enter Base Value : '))
exp = int(input('Enter Exponential Value : '))
res = Power(base, exp)
print(res)