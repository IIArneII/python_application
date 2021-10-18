from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMainWindow, QPushButton, QSizePolicy
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


class HopfieldNetApp(QMainWindow, HopfieldNetUI):
    def __init__(self, n):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.n = n
        self.holpfield = HopfieldNet(n)
        self.drow1_btns = []
        self.drow2_btns = []
        self.initUI()

    def initUI(self):
        for i in range(self.n):
            temp = []
            for j in range(self.n):
                btn = QPushButton('', self)
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

    def fit(self):
        temp = np.ones((self.n, self.n)) * (-1)
        for i in range(len(self.drow1_btns)):
            for j in range(len(self.drow1_btns[i])):
                if self.drow1_btns[i][j].isChecked():
                    temp[i][j] = 1
        self.holpfield.fit(temp)

    def recognize(self):
        temp = np.ones((self.n, self.n)) * (-1)
        for i in range(len(self.drow1_btns)):
            for j in range(len(self.drow1_btns[i])):
                if self.drow1_btns[i][j].isChecked():
                    temp[i][j] = 1
        resp, t = self.holpfield.recognize(temp)


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
    w = HopfieldNetApp(50)
    w.show()
    sys.exit(app.exec())