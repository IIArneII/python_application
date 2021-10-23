import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from task1_ui import Ui_MainWindow


class RandLineApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.btn_start.clicked.connect(self.btn_clicked)
        self.btn_obz.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        if self.sender() == self.btn_obz:
            self.line_file.setText(QFileDialog.getOpenFileName()[0])
        if self.sender() == self.btn_start:
            f = open(self.line_file.text(), 'r')
            lines = f.readlines()
            f.close()
            if lines:
                self.text_1.setText(random.choice(lines))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = RandLineApp()
    w.show()
    sys.exit(app.exec())