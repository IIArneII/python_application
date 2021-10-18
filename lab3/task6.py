import sys
import pickle
import re
from passwordError import *
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMainWindow, QFileDialog
from PyQt5.QtCore import QTime, QDate, Qt
from login_ui import LoginUI
from task5 import check_phone
from task3 import check_password


class LoginApp(QMainWindow, LoginUI):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.btn_log_in.setEnabled(False)
        self.line_password.textChanged.connect(self.line_changed)
        self.line_login.textChanged.connect(self.line_changed)
        self.line_phone.textChanged.connect(self.line_changed)
        self.btn_log_in.clicked.connect(self.btn_clicked)

    def line_changed(self):
        if self.line_password.text() and self.line_login.text() and self.line_phone.text():
            self.btn_log_in.setEnabled(True)
        else:
            self.btn_log_in.setEnabled(False)

    def btn_clicked(self):
        try:
            check_phone(self.line_phone.text())
            check_password(self.line_password.text())
            self.lbl_info.setText("Вы удачно зарегистрировались")
        except Exception as e:
            self.lbl_info.setText(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LoginApp()
    w.show()
    sys.exit(app.exec())

