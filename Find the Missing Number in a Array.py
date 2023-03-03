# Python Program to print the missing Number in a givven array.

x = []
for i in range(1, 8):
    if i == 3:
        continue
    else:
        x.append(i)
def find_Missing_Number(array, n):
    res = n*(n+1)//2
    z = sum(x)
    output = res - z
    print(output)
find_Missing_Number(x, 7)

