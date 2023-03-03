# Python Program to print the common letters in two strings.

data_1 = input('Enter Any String : ')
data_2 = input('Enter Any String : ')

x, y = set(data_1), set(data_2)

result = x & y
print(result)