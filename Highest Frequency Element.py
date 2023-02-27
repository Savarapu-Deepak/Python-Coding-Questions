# Python Program to print the highest frequency number

data = [1, 2, 3, 4, 2, 4, 5, 1, 2, 2, 3, 5, 5, 2, 2, 2, 4]
count = 0
for item in data:
    res = data.count(item)
    if res > count:
        count = res
        num = item
else:
    print(num, count)