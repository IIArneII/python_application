def subsequence(line1, line2):
    table = [[0 for _ in range(len(line2))] for _ in range(len(line1))]
    for i in range(len(line1)):
        for j in range(len(line2)):
            if (i == 0 or j == 0) and line1[i] == line2[j]:
                table[i][j] = 1
            elif i == 0 and line1[i] != line2[j]:
                table[i][j] = table[i][j-1]
            elif j == 0 and line1[i] != line2[j]:
                table[i][j] = table[i - 1][j]
            elif line1[i] == line2[j]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max([table[i - 1][j], table[i][j - 1]])
    return table[-1][-1]


if __name__ == '__main__':
    word = input('Изначальное слово: ')
    words = input('Похожиес слова через запятую с пробелом: ')
    words = words.split(', ')
    subs = {}
    for i in words:
        subs[i] = subsequence(word, i)
    subs = sorted(list(subs.items()), key=lambda x: x[1], reverse=True)
    subs = [i[0] for i in subs if i[1] == subs[0][1]]
    print(subs)


