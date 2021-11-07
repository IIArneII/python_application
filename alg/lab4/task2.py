import sympy


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

    def replace(self, pos, item):
        current = self.head
        found = False
        i = 0
        while not found:
            if i == pos:
                found = True
            else:
                current = current.getNext()
                i += 1
        current.setData(item)

        return i

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

    def get(self, pos):
        current = self.head
        i = 0
        while i < pos:
            current = current.getNext()
            i += 1
        return current.getData()

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


class HashTable:
    def __init__(self):
        self.size = 3
        self.slots = [UnorderedList() for i in range(self.size)]
        self.data = [UnorderedList() for i in range(self.size)]

    def put(self, key, data, resize=True):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue].isEmpty():
            self.slots[hashvalue].add(key)
            self.data[hashvalue].add(data)
        else:
            if self.slots[hashvalue].search(key):
                self.data[hashvalue].replace(self.slots[hashvalue].index(key), data)  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while not self.slots[nextslot].isEmpty() and not self.slots[nextslot].search(key):
                    nextslot = self.rehash(hashvalue, len(self.slots))

                if self.slots[nextslot].isEmpty():
                    self.slots[nextslot].add(key)
                    self.data[nextslot].add(data)
                else:
                    self.data[nextslot].replace(self.slots[nextslot].index(key), data)  # replace
        if resize:
            self.resize()

    def resize(self):
        if self.load() > 0.7:
            self.size = sympy.nextprime(self.size * 2) + 1
            slot = self.slots.copy()
            data = self.data.copy()
            self.slots = [None] * self.size
            self.data = [None] * self.size
            for i in range(len(slot)):
                if slot[i]:
                    self.put(slot[i], data[i], False)
        elif self.load() <= 0.2:
            self.size = sympy.prevprime(self.size / 2) + 1
            slot = self.slots.copy()
            data = self.data.copy()
            self.slots = [None] * self.size
            self.data = [None] * self.size
            for i in range(len(slot)):
                if slot[i]:
                    self.put(slot[i], data[i], False)

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def load(self):
        return sum([1 for i in self.slots if not i.isEmpty()]) / len(self.slots)

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while not self.slots[position].isEmpty() and not found and not stop:
            if self.slots[position].search(key):
                found = True
                data = self.data[position].get(self.slots[position].index(key))
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def delete(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        stop = False
        found = False
        position = startslot
        while not self.slots[position].isEmpty() and not found and not stop:
            if self.slots[position].search(key):
                found = True
                self.data[position].pop(self.slots[position].index(key))
                self.slots[position].pop(self.slots[position].index(key))
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        self.resize()

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        return sum([i.size() for i in self.slots])

    def __contains__(self, key):
        if self.get(key):
            return True
        return False

    def __delitem__(self, key):
        self.delete(key)