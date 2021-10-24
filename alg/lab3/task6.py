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

if __name__ == '__main__':
    html = '<html><head><title>Example</title></head><body><h1>Hello, world</h1></body></html>'
    html = re.findall('<[/\w]+>', html)
    stack = Stack()
    for i in html:
        if stack.isEmpty() or i[1] != '/':
            stack.push(i)
        elif i[1] == '/' and stack.peek() == re.sub('/', '', i):
            stack.pop()
        else:
            break
    if not stack.isEmpty():
        print('Баланс нарушен')
    else:
        print('Баланс не нарушен')

