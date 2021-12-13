def substring(line1, line2):
    table = [[0 for _ in range(len(line2))] for _ in range(len(line1))]
    for i in range(len(line1)):
        for j in range(len(line2)):
            if (i == 0 or j == 0) and line1[i] == line2[j]:
                table[i][j] = 1
            elif line1[i] == line2[j]:
                table[i][j] = table[i - 1][j - 1] + 1
    return max(max(table, key=lambda x: max(x)))


if __name__ == '__main__':
    word = input('Изначальное слово: ')
    words = input('Похожиес слова через запятую с пробелом: ')
    words = words.split(', ')
    subs = {}
    for i in words:
        subs[i] = substring(word, i)
    subs = sorted(list(subs.items()), key=lambda x: x[1], reverse=True)
    subs = [i[0] for i in subs if i[1] == subs[0][1]]
    print(subs)


