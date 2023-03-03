# Find Out Pairs with given sum in an array.
check = int(input('Enter Any Integer Value : '))
data_1 = [3, 4, 5, 7, 8, 9, 19, 11]
for x in range(len(data_1)):
    for y in range(x+1, len(data_1)):
        if data_1[x] + data_1[y] == check:
            print(data_1[x],',', data_1[y])


