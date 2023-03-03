# Python Program to reverse words in a String.
data = 'NetSet is an Online Platform'
data = data.split()
result = []
for item in data:
    result.insert(0, item)
else:
    output = ' '.join(result)
    print(output)