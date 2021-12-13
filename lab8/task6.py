import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QGuiApplication
from ui.task6_ui import Ui_MainWindow


class Task6App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Task6App, self).__init__()
        self.setupUi(self)
        self.clipboard = QGuiApplication.clipboard()
        self.init_ui()

    def init_ui(self):
        self.btn1.clicked.connect(self.btn_clicked)
        self.btn2.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        if self.sender() == self.btn1:
            self.clipboard.setText(self.text1.toPlainText())
        if self.sender() == self.btn2:
            self.text2.setText(self.clipboard.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task6App()
    w.show()
    sys.exit(app.exec())
