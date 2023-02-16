# Python Program to print Average of Numbers.
num = int(input('Enter total number of numbes : '))
sum = 0
for i in range(1, num + 1):
    x = int(input('Enter Number_{} :'.format(i)))
    sum = sum + x
else:
    average = sum / num
    print('-' * 20)
    print('Average :', average)
