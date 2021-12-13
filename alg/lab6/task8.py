import random
from collections import Counter

def new_len(a):
    if float('inf') in a:
        return float('inf')
    return len(a)


def atm_dynamic(n, coins=[100, 50, 10, 4, 3, 1]):
    table = [[float('inf')] for _ in range(n + 1)]
    table[0] = []
    for j in range(1, n + 1):
        for i in range(len(coins)):
            if j >= coins[i] and new_len(table[j - coins[i]]) + 1 < new_len(table[j]):
                table[j] = table[j - coins[i]].copy() + ([coins[i]])
    return table[n]


if __name__ == '__main__':
    coins = {1: 1, 3: 10, 4: 10, 10: 5, 50: 5, 100: 5}
    clients = 4
    clients = [random.randint(10, 200) for _ in range(clients)]
    for i in clients:
        print(f'Клиент хочет {i} руб.', end=' ')
        atm = atm_dynamic(i, list(coins.keys()))
        n = Counter(atm)
        get = True
        for j in n:
            if coins[j] - n[j] < 0:
                print('- невозможно снять')
                get = False
                break

        if get:
            for j in n:
                coins[j] -= n[j]
                if coins[j] == 0:
                    del coins[j]
            print('- ', atm)
        print('Остаток:', coins, end='\n\n')
