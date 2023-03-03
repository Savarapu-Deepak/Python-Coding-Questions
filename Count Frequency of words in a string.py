# Pyrhon Program to count the frequency of words in string.

data = 'Sheena loves eating Apple and Mango. Her Sister also loves eating Apple and Mango.'
data_1, result = data.split(), {}
for item in data_1:
    if item not in result:
        result[item] = 1
    else:
        result[item] += 1
else:
    print(result)
