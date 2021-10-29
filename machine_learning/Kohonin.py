import numpy as np


class KohoninNet:
    def __init__(self, n, inp):
        self.n = n
        self.inp = inp
        self.weights = np.random.rand(n, inp)

    def norm(self, x, y):
        return np.sum(np.abs(x - y), axis=1)

    def fit(self, x, epoch=1):
        for er in range(epoch):
            for s in x:
                norms = self.norm(self.weights, s)
                c = np.argmin(norms)


k = KohoninNet(2, 3)
print(k.weights, '\n')
k.fit([1, 2, 3])
