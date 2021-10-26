from task1 import UnorderedList
from matplotlib import pyplot as plt
import timeit


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class UnorderedStack:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items.head.getData()

    def size(self):
        return self.items.size()


class UnorderedQueue:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return self.items.size()


class UnorderedDeque:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def addFront(self, item):
        self.items.add(item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return self.items.size()


if __name__ == '__main__':
    l = UnorderedDeque()
    l.addFront(0)
    l.addFront(1)
    l.addRear(2)
    l.addRear(3)
    print(l.items)
    print(l.removeFront())
    print(l.removeRear())
    print(l.items)
    print(l.size())
    print(l.isEmpty())

    if False:
        t1 = timeit.Timer("a1.addFront(j)", globals=globals())
        t2 = timeit.Timer("a2.addFront(j)", globals=globals())

        y1 = []
        y2 = []
        x = []
        for i in range(1000, 10000, 100):
            a1 = UnorderedDeque()
            a2 = Deque()
            x.append(i)
            sum_y1 = 0
            sum_y2 = 0
            for j in range(i):
                sum_y1 += t1.timeit(number=10)
                sum_y2 += t2.timeit(number=10)
            y1.append(sum_y1)
            y2.append(sum_y2)
            print(i)

        plt.plot(x, y1, 'b', label='UnorderedDeque - addFront')
        plt.plot(x, y2, 'r', label='Deque - addFront')
        plt.legend()
        plt.show()


