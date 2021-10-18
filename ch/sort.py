import turtle
import random
import matplotlib.pyplot as plt
import numpy as np
import timeit


def sort_by_selection(x):
    for i in range(len(x)):
        min = i
        for j in range(i + 1, len(x)):
            if x[min] > x[j]:
                min = j
        x[i], x[min] = x[min], x[i]
    return x


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


timer1 = timeit.Timer("sort_by_selection(a)", globals=globals())
timer2 = timeit.Timer("quicksort(a)", globals=globals())

x = []
y11 = []
y12 = []
y13 = []
y21 = []
y22 = []
y23 = []
for i in range(500, 10000, 500):
    x.append(i)
    # Сортировка выбором
    a = list(np.random.randint(0, 10, i))  # Случайный массив
    y11.append(timer1.timeit(number=1))

    a = list(np.arange(0, i, 1))  # Отсортированный массив
    y12.append(timer1.timeit(number=1))

    a = list(np.arange(i, 0, -1))  # Отсортированный наоборот массив
    y13.append(timer1.timeit(number=1))

    # Быстрая сортировка
    a = list(np.random.randint(0, 10, i))  # Случайный массив
    y21.append(timer2.timeit(number=1))

    a = list(np.arange(0, i, 1))  # Отсортированный массив
    y22.append(timer2.timeit(number=1))

    a = list(np.arange(i, 0, -1))  # Отсортированный наоборот массив
    y23.append(timer2.timeit(number=1))

    print(i)

plt.plot(x, y11, 'r', label='Выбором - случайный')
plt.plot(x, y12, 'b--', label='Выбором - отсортированный')
plt.plot(x, y13, 'c--', label='Выбором - отсортированный наоборот')
plt.plot(x, y21, 'g', label='Быстрая - случайный')
plt.plot(x, y22, 'y--', label='Быстрая - отсортированный')
plt.plot(x, y23, 'm--', label='Быстрая - отсортированный наоборот')
plt.legend()
plt.show()
