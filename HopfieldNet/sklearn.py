import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils.extmath import cartesian

def f(x, y):
    z = cartesian(x, y)
    return z

plt.contourf([1, 2, 3], [1, 2, 3], [[2, 1, 2], [1, 2, 1], [2, 1, 2]])
plt.show()