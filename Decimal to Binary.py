# Python Program to Convert Deciamal to Binary.

def decimal_To_Binary(n):
    assert int(n) == n, 'Positive Integer Only'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_To_Binary(n // 2)
print(decimal_To_Binary(10))
