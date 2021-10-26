from PIL import Image
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from ui.task1_ui import Ui_MainWindow

class Task1App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.pixmap = QPixmap()
        self.init_ui()

    def init_ui(self):
        file = QFileDialog.getOpenFileName()[0]
        self.pixmap.load(file)
        pil = self.pixmap.toImage()
        print(pil)
        self.label.setPixmap(self.pixmap)

        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        if self.sender() == self.pushButton:
            self.label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task1App()
    w.show()
    sys.exit(app.exec())
