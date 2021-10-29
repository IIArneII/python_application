from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMainWindow, QPushButton, QSizePolicy
from PyQt5 import QtGui
from hopfield_ui import HopfieldNetUI
import numpy as np
import sys


class HopfieldNet():
    def __init__(self, n):
        self.sh = n
        self.n = n * n
        self.t_max = 100
        self.weights = np.zeros((self.n, self.n))

    def sig(self, x):
        if x >= 0:
            return 1
        else:
            return -1

    def fit(self, x):
        x = x.reshape(self.n)
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    self.weights[i][j] += x[i] * x[j]
                else:
                    self.weights[i][j] = 0

    def recognize(self, x):
        x = x.reshape(self.n)
        current_state = x.copy()
        prev_state = current_state.copy()

        for i in range(self.n):
            sum = 0
            for j in range(self.n):
                sum += self.weights[i][j] * prev_state[j]
            current_state[i] = self.sig(sum)

        t = 0
        while not np.array_equal(current_state, prev_state) and t < self.t_max:
            t += 1
            prev_state = current_state.copy()
            for i in range(self.n):
                sum = 0
                for j in range(self.n):
                    sum += self.weights[i][j] * prev_state[j]
                current_state[i] = self.sig(sum)

        return (current_state.reshape(self.sh, self.sh), t)


class HammingNet:
    def __init__(self, m, eps=0.000000001):
        self.eps = eps
        self.k = 0  # Количество образцов
        self.m = m  # Размерность
        self.x = np.array([])
        self.w1 = np.array([])
        self.w2 = np.array([])

    def add(self, x):
        self.k += 1
        if self.k == 1:
            self.x = np.array(x).reshape((1, self.m))
        else:
            temp = np.array(x).reshape((1, self.m))
            self.x = np.append(self.x, temp, axis=0)

    def activation(self, s):
        if s < 0:
            return 0
        if s < self.m / 2:
            return s
        return self.m / 2

    def norm(self, x, y):
        return np.sqrt(np.sum((y - x) ** 2))

    def fit(self):
        self.w1 = self.x / 2
        self.w2 = -np.random.random((self.k, self.k)) / self.k
        np.fill_diagonal(self.w2, 1)

    def evaluate(self, a):
        y1 = np.dot(self.w1, np.array(a).reshape(-1))
        for i in range(len(y1)):
            y1[i] = self.activation(y1[i])
        y2 = np.dot(self.w2, y1)
        for i in range(len(y2)):
            y2[i] = self.activation(y2[i])
        t = 1
        while self.norm(y1, y2) > self.eps and t < 100:
            y1 = y2
            y2 = np.dot(self.w2, y1)
            for i in range(len(y2)):
                y2[i] = self.activation(y2[i])
            t += 1

        return self.x[np.argmax(y2)], t


class HopfieldNetApp(QMainWindow, HopfieldNetUI):
    def __init__(self, n):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.n = n
        self.hamming = HammingNet(n * n)
        self.drow1_btns = []
        self.drow2_btns = []
        self.initUI()

    def mouse_btn(self, e: QtGui.QMouseEvent) -> None:
        x, y = e.windowPos().x(), e.windowPos().y()
        for i in self.drow1_btns:
            for j in i:
                if (j.x() < x - 12) and (j.x() + j.width() > x - 12) and (j.y() < y - 12) and (
                        j.y() + j.height() > y - 12):
                    if self.checkBox.isChecked():
                        j.setChecked(False)
                    else:
                        j.setChecked(True)

    def initUI(self):
        for i in range(self.n):
            temp = []
            for j in range(self.n):
                btn = QPushButton('', self)

                btn.mouseMoveEvent = self.mouse_btn

                btn.setCheckable(True)
                btn.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
                self.drow1.addWidget(btn, i, j)
                temp.append(btn)
            self.drow1_btns.append(temp)

        for i in range(self.n):
            temp = []
            for j in range(self.n):
                btn = QPushButton('', self)
                btn.setCheckable(True)
                btn.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
                self.drow2.addWidget(btn, i, j)
                temp.append(btn)
            self.drow2_btns.append(temp)

        self.clear_btn.clicked.connect(self.clear)
        self.remember_btn.clicked.connect(self.fit)
        self.recognize_btn.clicked.connect(self.recognize)

    def clear(self):
        for i in self.drow1_btns:
            for j in i:
                j.setChecked(False)

    def add_pattern(self, x):
        text = '\n'
        for i in x:
            for j in i:
                if j == -1:
                    text = text + '□  '
                else:
                    text = text + '■  '
            text = text + '\n'
        self.text.append(text)

    def fit(self):
        temp = np.ones((self.n, self.n)) * (-1)
        for i in range(len(self.drow1_btns)):
            for j in range(len(self.drow1_btns[i])):
                if self.drow1_btns[i][j].isChecked():
                    temp[i][j] = 1
        self.add_pattern(temp)
        self.hamming.add(np.array(temp))
        self.hamming.fit()

    def recognize(self):
        temp = np.ones((self.n, self.n)) * (-1)
        for i in range(len(self.drow1_btns)):
            for j in range(len(self.drow1_btns[i])):
                if self.drow1_btns[i][j].isChecked():
                    temp[i][j] = 1
        resp, t = self.hamming.evaluate(np.array(temp))
        print(resp)
        print(t, '\n')
        resp = resp.reshape((self.n, self.n))
        for i in self.drow2_btns:
            for j in i:
                j.setChecked(False)

        for i in range(len(self.drow1_btns)):
            for j in range(len(self.drow1_btns[i])):
                if resp[i][j] == 1:
                    self.drow2_btns[i][j].setChecked(True)
        print(t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HopfieldNetApp(7)
    w.show()
    sys.exit(app.exec())
