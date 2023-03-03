# Python Program to convert two list into Dictionary.

list_1 = ['Naina', 'Sheena', 'Kimi']
list_2 = [853245, 769852, 123456]
result = dict(zip(list_1, list_2))
print(result)

# Python Program to convert above dictionary to tuple.

for item in result.items():
    print(tuple(item))