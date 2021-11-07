import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


class KohoninNet:
    def __init__(self, n, inp):
        self.n = n
        self.inp = inp + 1
        self.l = 0.1
        self.sig = 0.6
        self.weights = np.random.rand(n, inp + 1)

    def norm(self, x, y):
        if x.shape == (self.inp,):
            return np.sum(np.abs(x - y))
        return np.sum(np.abs(x - y), axis=1)

    def fit(self, x, epoch=1):
        x = np.append(x, np.ones((len(x), 1)), axis=1)
        for er in range(epoch):
            e = 0
            for i in x:
                c = np.argmin(self.norm(self.weights, i))
                for j in range(len(self.weights)):
                    h = self.l * np.exp((-self.norm(self.weights[j], self.weights[c]) ** 2) / (2 * self.sig ** 2))
                    row = self.weights[j] + h * (i - self.weights[j])
                    self.weights[j] = row
                plt.plot(self.weights[:, 0], self.weights[:, 1], 'c.')
                e += self.norm(self.weights[c], i)
            e = e / self.n
            print(f'er: {er}\te: {e}')

    def response(self, x):
        x = np.append(x, np.ones((len(x), 1)), axis=1)
        y = np.dot(x, self.weights.transpose())
        for i in range(len(y)):
            max = np.argmax(y[i])
            y[i] = y[i] * 0
            y[i][max] = 1
        return y


def funk(x, y, f):
    s = []
    for j in x:
        s.append([])
        for i in y:
            s[-1].append(np.argmax(f([[i, j]])[0]))
    return s


x1 = np.random.normal(loc=(-1, 1), size=(20, 2), scale=0.2)
x2 = np.random.normal(loc=(-0.5, -0.5), size=(20, 2), scale=0.2)
x3 = np.random.normal(loc=(1, 1), size=(20, 2), scale=0.2)
x1 = np.append(x1, x2, axis=0)
x1 = np.append(x1, x3, axis=0)

k = KohoninNet(3, 2)
k.fit(x1, epoch=100)

resp = k.response(x1)

for i in range(len(x1)):
    plt.plot(x1[i][0], x1[i][1], 'r.')
# for i in range(len(k.weights)):
#     plt.text(k.weights[i][0], k.weights[i][1], f'{i}')
for i in range(len(resp)):
    plt.text(x1[i][0], x1[i][1], f'{np.argmax(resp[i])}')
plt.plot(k.weights[:, 0], k.weights[:, 1], 'ko')

x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
plt.contourf(x, y, funk(x, y, k.response))

plt.show()
