import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QKeyEvent, QPixmap
from PyQt5.QtCore import Qt
from ui.task5_ui import Ui_MainWindow


class Task4App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        pix = QPixmap('img/нло.PNG')
        self.lbl.setGeometry(self.lbl.x(), self.lbl.y(), pix.width(), pix.height())
        self.lbl.setPixmap(pix)

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Right:
            self.lbl.move(self.lbl.x() + 10, self.lbl.y())
        if e.key() == Qt.Key_Left:
            self.lbl.move(self.lbl.x() - 10, self.lbl.y())
        if e.key() == Qt.Key_Up:
            self.lbl.move(self.lbl.x(), self.lbl.y() - 10)
        if e.key() == Qt.Key_Down:
            self.lbl.move(self.lbl.x(), self.lbl.y() + 10)
        if self.lbl.x() + self.lbl.width() / 2 < 0:
            self.lbl.move(int(self.width() - self.lbl.width() / 2), self.lbl.y())
        if self.lbl.x() + self.lbl.width() / 2 > self.width():
            self.lbl.move(0, self.lbl.y())
        if self.lbl.y() + self.lbl.height() / 2 < 0:
            self.lbl.move(self.lbl.x(), int(self.height() - self.lbl.height() / 2))
        if self.lbl.y() + self.lbl.height() / 2 > self.height():
            self.lbl.move(self.lbl.x(), 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task4App()
    w.show()
    sys.exit(app.exec())
