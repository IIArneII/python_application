import sympy


class HashTable:
    def __init__(self):
        self.size = 11 + 1
        self.skip = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data, resize=True):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                self.skip = 0
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(hashvalue, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace
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
        self.skip += 1
        return (oldhash + self.skip ** 2) % size

    def load(self):
        return self.__len__() / len(self.slots)

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        self.skip = 0
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
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
        self.skip = 0
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                self.data[position] = None
                self.slots[position] = None
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
        return len(self.slots) - self.slots.count(None)

    def __contains__(self, key):
        if self.get(key):
            return True
        return False

    def __delitem__(self, key):
        self.delete(key)


t = HashTable()
t.put(3, 3)
t.put(14, 14)
t.put(25, 25)
t.put(36, 36)
t.put(47, 47)
# t.put(58, 58)
# t.put(69, 69)
# t.put(80, 80)
# t.put(91, 91)
print(t.slots)
print(t.data)
del t[47]
del t[14]
del t[36]
print(t.slots)
print(t.data)
