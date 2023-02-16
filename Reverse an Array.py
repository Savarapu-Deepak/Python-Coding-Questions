# Python program to revere an array.

import numpy as np

x = np.array([25, 78, 98, 10, 789, 20])
res = np.flip(x)
print(res)
print(x[::-1])