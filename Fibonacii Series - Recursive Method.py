# Python Program to print Fibonacii Series Using Recursive Method.

def Fibonacii(n):
    assert n >= 0 and int(n) == n, 'Positive Integer Only..'
    if n in [0, 1]:
        return n
    else:
        return Fibonacii(n - 1) + Fibonacii(n - 2)
num = int(input('Enter Fibonacii Range : '))
print(Fibonacii(num))

