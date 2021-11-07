import sys
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.task4_ui import Ui_Form


class Task4App(QMainWindow, Ui_Form):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setMouseTracking(True)

    def bX(self):
        return self.btn.x() + 50

    def bY(self):
        return self.btn.y() + 50

    def len_v(self, v):
        return np.sqrt(v[0] ** 2 + v[1] ** 2)

    def mouseMoveEvent(self, e):
        v = (self.bX() - e.x(), self.bY() - e.y())
        l = self.len_v(v)
        if l < 100 and \
                (self.bX() > 60 or v[0] > 0) and \
                (self.bY() > 60 or v[1] > 0) and \
                (self.bX() < self.width() - 60 or v[0] < 0) and \
                (self.bY() < self.height() - 60 or v[1] < 0):
            new_x = int(self.btn.x() + (v[0] * 10 / l))
            new_y = int(self.btn.y() + (v[1] * 10 / l))
            self.btn.move(new_x, new_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task4App()
    w.show()
    sys.exit(app.exec())
