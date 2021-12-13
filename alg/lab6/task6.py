import random as r


def greedy1(items):
    boxes = [0]
    for i in items:
        for j in range(len(boxes)):
            if i + boxes[j] <= 1:
                boxes[j] += i
                break
            if j == len(boxes) - 1:
                boxes.append(i)
    return len(boxes)


def greedy2(items):
    boxes = [0]
    for i in items:
        boxes.sort(reverse=True)
        for j in range(len(boxes)):
            if i + boxes[j] <= 1:
                boxes[j] += i
                break
            if j == len(boxes) - 1:
                boxes.append(i)
    return len(boxes)


def greedy3(items):
    boxes = [0]
    j = 0
    for i in items:
        if i + boxes[j] <= 1:
            boxes[j] += i
        else:
            j += 1
            boxes.append(i)
    return len(boxes)


def greedy4(items):
    boxes = [0]
    for i in items:
        boxes.sort()
        for j in range(len(boxes)):
            if i + boxes[j] <= 1:
                boxes[j] += i
                break
            if j == len(boxes) - 1:
                boxes.append(i)
    return len(boxes)


if __name__ == '__main__':
    items = [[r.randint(1, 10) / 10 for _ in range(0, 50)],
             [r.randint(1, 10) / 10 for _ in range(0, 100)],
             [r.randint(1, 10) / 10 for _ in range(0, 200)],
             [r.randint(1, 10) / 10 for _ in range(0, 500)]]
    for i in items:
        print('Количество:', len(i))
        print('\t1 метод:', greedy1(i))
        print('\t2 метод:', greedy2(i))
        print('\t3 метод:', greedy3(i))
        print('\t4 метод:', greedy4(i))
