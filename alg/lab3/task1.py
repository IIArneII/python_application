class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        previous = None
        while current:
            previous = current
            current = current.getNext()
        new_item = Node(item)
        previous.setNext(new_item)

    def index(self, item):
        current = self.head
        found = False
        i = 0
        while not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                i += 1

        return i

    def insert(self, pos, item):
        current = self.head
        previous = None
        i = 0
        while i < pos:
            previous = current
            current = current.getNext()
            i += 1
        temp = Node(item)
        temp.setNext(current)
        previous.setNext(temp)

    def pop(self, pos=None):
        if pos or pos == 0:
            current = self.head
            previous = None
            i = 0
            while i < pos:
                previous = current
                current = current.getNext()
                i += 1
            if pos != 0:
                previous.setNext(current.getNext())
            else:
                self.head = current.getNext()
            return current.getData()
        else:
            return self.pop(self.size() - 1)

    def __str__(self):
        l = []
        current = self.head
        while current:
            l.append(current.getData())
            current = current.getNext()
        return str(l)

    def __getitem__(self, item):
        temp = UnorderedList()
        current = self.head
        i = 0
        while i < item.stop:
            if i == item.start:
                temp.add(current.getData())
            if i > item.start:
                temp.append(current.getData())
            current = current.getNext()
            i += 1
        return temp


if __name__ == '__main__':
    l = UnorderedList()
    l.add(0)
    l.add(1)
    l.append(2)
    l.append(3)
    print(l)
    print(l[1:3])
    print(l.index(0))
    l.insert(2, 222)
    print(l)
    l.pop()
    print(l)
    l.pop(1)
    print(l)
