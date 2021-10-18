class DefaultList(list):
    def __init__(self, default):
        super().__init__()
        self.default = default

    def __getitem__(self, item):
        try:
            temp = super().__getitem__(item)
            return temp
        except IndexError:
            return self.default


if __name__ == '__main__':
    s = DefaultList('default')
    s.extend([1, 5, 7])
    indexes = [0, 2, 1000, -1]
    for i in indexes:
        print(s[i], end=" ")
