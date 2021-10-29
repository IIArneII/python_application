import sys
import random as r
from PyQt5.QtGui import QPainter, QColor, QPaintEvent
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QMainWindow
from ui.task3_ui import Ui_MainWindow


class Task3App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.i = 1
        self.initUI()

    def initUI(self):
        self.i = QInputDialog.getInt(self, 'Количество полос', 'Введите количество полос флага (1 по умолчанию)',
                                     value=1, min=1, max=10)[0]
        self.setGeometry(300, 300, 50 * self.i + 60, 60 + 30 * self.i)
        self.setFixedSize(self.width(), self.height())

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        for j in range(self.i):
            qp.setBrush(QColor(r.randrange(0, 255), r.randrange(0, 255), r.randrange(0, 255)))
            qp.drawRect(30, 30 + 30 * j, 50 * self.i, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task3App()
    ex.show()
    sys.exit(app.exec())
