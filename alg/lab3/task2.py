from task1 import UnorderedList


def move_to_front(n):
    l = UnorderedList()
    for i in range(n):
        line = input()
        if l.search(line):
            l.remove(line)
        l.add(line)
    return l


if __name__ == '__main__':
    print(move_to_front(5))
