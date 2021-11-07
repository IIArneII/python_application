import numpy as np

row1 = 0.5
for i in range(100):
    row2 = row1 + 0.9 * (2 + row1)
    row1 = row2
    print(row1)
