import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


class KohoninNet:
    def __init__(self, n, inp, ring=False):
        self.n = n
        self.inp = inp
        self.l = 0.1
        self.sig = 0.3
        self.weights = np.random.rand(n, inp)

    def norm(self, x, y):
        # if x.shape == (self.inp,):
        #     x1, y1 = x[0], x[1]
        #     x2, y2 = y[0], y[1]
        #     return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        #
        # x1, y1 = x[:, 0], x[:, 1]
        # if y.shape == (self.inp,):
        #     x2, y2 = y[0], y[1]
        # else:
        #     x2, y2 = y[:, 0], y[:, 1]
        # return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if x.shape == (self.inp,):
            return np.sum(np.abs(x - y))
        return np.sum(np.abs(x - y), axis=1)

    def fit(self, x, epoch=1):
        for er in range(epoch):
            e = 0
            for i in x:
                c = np.argmin(self.norm(self.weights, i))
                for j in range(len(self.weights)):
                    h = self.l * np.exp((-(self.norm(self.weights[j], self.weights[c])) ** 2) / (2 * self.sig ** 2))
                    row = self.weights[j] + h * (i - self.weights[j])
                    self.weights[j] = row
                    plt.plot(self.weights[j][0], self.weights[j][1], 'c.')
                e += self.norm(self.weights[c], i)
            e = e / self.n
            print(f'er: {er}\te: {e}')

    def fit_tsp(self, x, epoch=1):
        for er in range(epoch):
            e = 0

            if er % 1 == 0:
                plt.plot(x[:, 0], x[:, 1], 'r.')
                plt.plot(k.weights[:, 0], k.weights[:, 1], 'b')
                plt.savefig(f'D:/рэ/пуки/{er}.png', format='png')
                plt.clf()
            for i in x:
                c = np.argmin(self.norm(self.weights, i))

                j = c
                if j >= len(self.weights):
                    j = 0
                h = self.l * np.exp((-(self.norm(self.weights[j], self.weights[c])) ** 2) / (2 * self.sig ** 2))
                row = self.weights[j] + h * (i - self.weights[j])
                self.weights[j] = row

                j = c + 1
                if j >= len(self.weights):
                    j = 0
                h = self.l * np.exp((-(self.norm(self.weights[j], self.weights[c])) ** 2) / (2 * self.sig ** 2))
                row = self.weights[j] + h * (i - self.weights[j])
                self.weights[j] = row

                j = c - 1
                if j == -1:
                    j = len(self.weights) - 1
                h = self.l * np.exp((-self.norm(self.weights[j], self.weights[c]) ** 2) / (2 * self.sig ** 2))
                row = self.weights[j] + h * (i - self.weights[j])
                self.weights[j] = row

                e += self.norm(self.weights[c], i)
            e = e / self.n
            print(f'er: {er}\te: {e}')

    def response(self, x):
        y = []
        for i in x:
            min = np.argmin(self.norm(self.weights, i))
            ad = [0 if i != min else 1 for i in range(len(self.weights))]
            y.append(ad)
        return np.array(y)


        # print(np.sum(self.weights ** 2, axis=1))
        # y = np.dot(x, self.weights.transpose())
        # for i in range(len(y)):
        #     max = np.argmax(y[i])
        #     y[i] = y[i] * 0
        #     y[i][max] = 1
        # return y


def funk(x, y, f):
    s = []
    for j in x:
        s.append([])
        for i in y:
            s[-1].append(np.argmax(f(np.array([[i, j]]))[0]))
    return s


# x1 = np.random.normal(loc=(0.5, 0.5), size=(5, 2), scale=0.2)
# k = KohoninNet(5, 2)
# k.fit_tsp(x1, epoch=50)
#
# for i in range(len(x1)):
#     plt.plot(x1[i][0], x1[i][1], 'r.')
# plt.plot(k.weights[:, 0], k.weights[:, 1], 'b')
#
# plt.show()

# x1 = np.random.normal(loc=(-1, 1), size=(20, 2), scale=0.2)
# x2 = np.random.normal(loc=(-0.5, -0.5), size=(20, 2), scale=0.2)
# x3 = np.random.normal(loc=(1, 1), size=(20, 2), scale=0.2)
x1 = np.random.normal(loc=(-1, 1), size=(20, 2), scale=0.2)
x2 = np.random.normal(loc=(0, 0), size=(20, 2), scale=0.2)
x3 = np.random.normal(loc=(1, -1), size=(20, 2), scale=0.2)
x1 = np.append(x1, x2, axis=0)
x1 = np.append(x1, x3, axis=0)

k = KohoninNet(3, 2)
k.fit(x1, epoch=10)

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
