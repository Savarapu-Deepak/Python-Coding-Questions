# Python Program to print Year is Leap year or not.

year = int(input('Enter Any Year : '))
if year % 4 == 0 or year % 100 == 0:
    print(year, 'is a Leap Year')
else:
    print(year, 'is not a Leap Year')
