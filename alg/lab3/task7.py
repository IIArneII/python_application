import re


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


def stack_calculator(line):
    try:
        stack = Stack()
        for i in line:
            if stack.isEmpty() or i not in ['+', '-', '*', '/']:
                stack.push(i)
            elif i in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                stack.push(str(eval(a + i + b)))
        if stack.size() != 1:
            return None
        else:
            return stack.pop()
    except:
        return None


if __name__ == '__main__':
    line = '0 2 3 + / '
    line = line.split()
    print(stack_calculator(line))
