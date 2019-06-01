import __future__

import numpy as np
import matplotlib.pyplot as plt

M = np.array([[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]])

M = np.array([[1, 0, 1],
              [0, 1, 0],
              [1, 0, 1]])

n = 4


def matkronpow(M, n):
    if n != 0:
        return np.kron(M, (matkronpow(M, n - 1)))
    else:
        return np.kron(M, M)


R = matkronpow(M, n)

plt.imshow(R)
plt.show()

