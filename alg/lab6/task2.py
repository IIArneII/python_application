import timeit
import random
from matplotlib import pyplot as plt

def copy(ceil):
    return {'cost': ceil['cost'], 'weight': ceil['weight'], 'items': ceil['items'].copy()}


def update(ceil, add):
    ceil['cost'] += add['cost']
    ceil['weight'] += add['weight']
    ceil['items'].update(add['items'])


def all_variants(items, limit, backpack=None):
    if not backpack:
        backpack = {'cost': 0, 'items': set(), 'weight': 0}
    max_cost = copy(backpack)
    for i in items:
        if items[i][0] not in backpack['items'] and items[i][1] + backpack['weight'] <= limit:
            temp = copy(backpack)
            temp['cost'] += items[i][2]
            temp['weight'] += items[i][1]
            temp['items'].add(items[i][0])
            temp = all_variants(items, limit, temp)
            if temp['cost'] > max_cost['cost']:
                max_cost = temp
    return max_cost


def greedy(items, limit):
    backpack = {'cost': 0, 'weight': 0, 'items': set()}
    itm = sorted(list(items.copy().values()), key=lambda x: x[2], reverse=True)
    while True:
        itm = [i for i in itm if i[1] + backpack['weight'] <= limit]
        if itm:
            backpack['cost'] += itm[0][2]
            backpack['weight'] += itm[0][1]
            backpack['items'].add(itm[0][0])
            del itm[0]
        else:
            return backpack


def dynamic(items, limit):
    table = [[{'cost': 0, 'items': set(), 'weight': 0} for _ in range(limit + 1)] for _ in range(len(items))]
    for i in range(len(table)):
        table[i][0]['items'].add(items[i][0])   # Заполняем нулевой столбик самими предметами
        table[i][0]['weight'] = items[i][1]
        table[i][0]['cost'] = items[i][2]

        for j in range(1, len(table[i])):
            if i == 0 and table[i][0]['weight'] <= j:
                # Если строчка первая и если предмет влазиет, копируем из нулевого стобика
                table[i][j] = copy(table[i][0])
            elif i != 0:
                if table[i][0]['weight'] > j:  # Если предмет не влазиет из нулевого столбика, копируем сверху
                    table[i][j] = copy(table[i - 1][j])
                else:
                    last_up = copy(table[i - 1][j])     # Смотрим ячейки сверху и слева
                    last_left = copy(table[i][j - 1].copy())

                    if table[i][0]['weight'] == j and table[i][0]['cost'] >= table[i][j - 1]['cost']:
                        # Если предмет в нулевом стобике выгоднее того, что левее, то берем из нулевого
                        last_left = copy(table[i][0])

                    table[i][j] = last_up
                    if last_left['cost'] >= last_up['cost']:
                        # Выбираем самый выгодный и добавляем в ячейку
                        table[i][j] = last_left

                    free = j - table[i][j]['weight']    # Смотрим оставшееся место в ячейке
                    if free > 0:
                        # Если место есть, ищем в подтаблице выше и левее до тех пор,
                        # пока не найдем подходящее по размеру, причем множество предметов
                        # в ячейках не должно пересекаться
                        for jj in range(free, -1, -1):
                            working = True
                            for ii in range(i, -1, -1):
                                if not table[i][j]['items'] & table[ii][jj]['items'] and table[ii][jj]['items'] and \
                                        table[ii][jj]['weight'] <= free:
                                    update(table[i][j], table[ii][jj])
                                    working = False
                                    break
                            if not working:
                                break
    return table[-1][-1]


def main():
    method = int(input('1 - полный перебор\n2 - жадный алгоритм\n3 - динамическое программирование\n'))
    limit = 6
    items = {0: ['вода', 3, 5], 1: ['книга', 1, 3], 2: ['еда', 2, 6], 3: ['куртка', 2, 5], 4: ['камера', 1, 6]}
    if method == 1:
        print(all_variants(items, limit))
    if method == 2:
        print(greedy(items, limit))
    if method == 3:
        print(dynamic(items, limit))


if __name__ == '__main__':
    # main()
    t1 = timeit.Timer("all_variants(items, limit)", globals=globals())
    t2 = timeit.Timer("greedy(items, limit)", globals=globals())
    t3 = timeit.Timer("dynamic(items, limit)", globals=globals())

    limit = 15
    items = {}
    x, yt1, yt2, yt3 = [], [], [], []
    for i in range(1, 20):
        print(i)
        items[i - 1] = [i, random.randint(1, 5), random.randint(1, 5)]
        x.append(i)
        yt1.append(t1.timeit(number=1))
        yt2.append(t2.timeit(number=1))
        yt3.append(t3.timeit(number=1))

    plt.plot(x, yt1, 'b', label='Полный перебор')
    plt.plot(x, yt2, 'g', label='Жадный алгоритм')
    plt.plot(x, yt3, 'r', label='Динамическое программирование')
    plt.legend()
    plt.show()
