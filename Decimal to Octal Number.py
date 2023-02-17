# Python Program to convert Decimal Number to Octal Number.

def decimal_to_Octal(n):
    assert int(n) == n, 'Positive Integer Only'
    if n == 0:
        return 0
    else:
        return n % 8 + 10 * decimal_to_Octal(n // 8)
print(decimal_to_Octal(64))
