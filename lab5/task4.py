import sys
import random as r
from PyQt5.QtGui import QPainter, QColor, QPaintEvent
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QMainWindow, QColorDialog
from PyQt5.QtCore import QPoint, QRectF
from ui.task2_ui import Ui_MainWindow


class Task3App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.color = None
        self.initUI()

    def initUI(self):
        self.color = QColorDialog.getColor()
        self.label.clear()
        self.slider.valueChanged.connect(self.slider_changed)

    def slider_changed(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        qp.setBrush(self.color)
        qp.drawEllipse(QPoint(int(self.width() / 2), int(self.height() / 2)), self.slider.value(), self.slider.value())
        qp.setBrush(QColor(200, 200, 255))
        qp.drawEllipse(
            QPoint(int(self.width() / 2 - self.slider.value() / 2), int(self.height() / 2 - self.slider.value() / 2)),
            self.slider.value() / 10, self.slider.value() / 10)
        qp.drawEllipse(
            QPoint(int(self.width() / 2 + self.slider.value() / 2), int(self.height() / 2 - self.slider.value() / 2)),
            self.slider.value() / 10, self.slider.value() / 10)
        qp.setBrush(QColor(0, 0, 0))
        qp.drawRect(int(self.width() / 2 - self.slider.value() / 2),
                    int(self.height() / 2 + self.slider.value() / 2),
                    self.slider.value(), int(self.slider.value() / 10))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task3App()
    ex.show()
    sys.exit(app.exec())
