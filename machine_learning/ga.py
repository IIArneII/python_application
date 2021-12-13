import random
from matplotlib import pyplot as plt

n = 100000

a = 0
for i in range(n):
    test = [random.randint(0, 99) for _ in range(91)]
    a += test.count(0)

print(a / n)
