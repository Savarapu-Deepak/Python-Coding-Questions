# Python Program to print Smallest Number among three..

x = int(input('Enter Number_1 :'))
y = int(input('Enter Number_2 :'))
z = int(input('Enter Number_3 : '))

if x < y and x < z:
    print(x,'is smallest among ',y,',',z)
elif y < z:
    print(y, 'is Smallest Number among ',z,',',x)
else:
    print(z, 'is smallest among ', x,',',y)