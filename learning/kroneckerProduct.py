import numpy as np

a = [[1, 2] , [3, 4]]
b = [[0, 5] , [6, 7]]

c = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
d = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]


print(np.kron(a,b))
print(np.kron(c,d))
