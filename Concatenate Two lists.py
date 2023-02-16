# Python Program to Concatenate two List.

list_1 = ['W', 'A', 'Wri', 'B']
list_2 = ['e', 're', 'ting', 'log']
res = [x+y for x, y in zip(list_1, list_2)]
print(res)