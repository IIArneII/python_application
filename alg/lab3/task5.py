class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoubleList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        temp.set_prev(None)
        if self.head:
            self.head.set_prev(temp)
        self.head = temp

    def append(self, item):
        current = self.head
        while current.get_next() and current:
            current = current.get_next()
        new_item = Node(item)
        new_item.set_next(None)
        new_item.set_prev(current)
        if current:
            current.set_next(new_item)
        else:
            self.head = new_item

    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        if not current.get_prev():
            self.head = current.get_next()
        else:
            current.get_prev().set_next(current.get_next())

    def insert_nex(self, pos, item):
        current = self.head
        i = 0
        while i < pos:
            current = current.get_next()
            i += 1
        temp = Node(item)
        temp.set_next(current.get_next())
        temp.set_prev(current)
        current.set_next(temp)

    def insert_prev(self, pos, item):
        current = self.head
        i = 0
        while i < pos:
            current = current.get_next()
            i += 1
        temp = Node(item)
        temp.set_next(current)
        temp.set_prev(current.get_prev())
        if current.get_prev():
            current.get_prev().set_next(temp)
        else:
            self.head = temp
        current.set_prev(temp)

    def pop_head(self):
        temp = self.head
        self.head = self.head.get_next()
        self.head.set_prev(None)
        return temp.get_data()

    def pop_end(self):
        current = self.head
        while current.get_next():
            current = current.get_next()
        current.get_prev().set_next(None)
        return current.get_data()

    def __str__(self):
        l = []
        current = self.head
        while current:
            l.append(current.get_data())
            current = current.get_next()
        return str(l)


if __name__ == '__main__':
    l = DoubleList()
    l.add(0)
    l.add(1)
    l.add(2)
    l.append(3)
    l.append(4)
    l.append(5)
    print(l)
    l.remove(0)
    print(l)
    print(l.search(0), ' ', l.search(1))
