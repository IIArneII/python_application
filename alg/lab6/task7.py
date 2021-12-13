def atm_greedy(n, coins=[100, 50, 10, 4, 3, 1]):
    give = []
    while sum(give) < n:
        for i in coins:
            if sum(give) + i <= n:
                give.append(i)
                break
    return give


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
    n = int(input('Количество монет: '))
    print('Жадный алгоритм:', atm_greedy(n))
    print('Динамическое программирование:', atm_dynamic(n))
