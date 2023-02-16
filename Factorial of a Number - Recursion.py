# Python Program to print Factorial of a number using Recursion Method.

def Factorial(n):
    assert n >=0 and int(n) ==n, 'Positive Integer Only'
    if n in [0, 1]:
        return n
    else:
        return n * Factorial(n - 1)
print(Factorial(int(input('Enter Any Number : '))))