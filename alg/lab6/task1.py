def print_table(table):
    for i in table:
        for j in i:
            print(j['cost'], j['items'], '    ', end='')
        print()


items = {1: ['вода', 3, 5], 2: ['книга', 1, 3], 3: ['еда', 2, 6], 4: ['куртка', 2, 5], 5: ['камера', 1, 6]}
limit = 6

table = [[{'cost': 0, 'items': []} for _ in range(6)] for _ in range(len(items))]
for i in range(len(table)):
    for j in range(len(table[i])):
        if i == 0 and items[i + 1][1] <= j + 1:
            table[i][j]['cost'] = items[i + 1][2]
            table[i][j]['items'].append(items[i + 1][0])
        else:
            cost = table[i - 1][j - items[i + 1][2]]['cost'] + table[i][j]['cost']
            if table[i - 1][j]['cost'] < cost:
                table[i][j]['items'].append(items[i + 1][0])
            table[i][j]['cost'] = max([table[i - 1][j]['cost'], cost])

print_table(table)
