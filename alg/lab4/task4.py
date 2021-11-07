from task3 import HashTable

line = 'Раз  раз раз как     меня слышно     Повторяю раз раз раз Повторяю'

h = HashTable()
for i in line.split():
    if i in h:
        h[i] += 1
    else:
        h[i] = 1
    print(h[i], '  ', end='')
