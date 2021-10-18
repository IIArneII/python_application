import sys
import pickle
import re
from passwordError import *
from phoneError import *
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMainWindow, QFileDialog
from PyQt5.QtCore import QTime, QDate, Qt
from password_ui import PasswordUI
from task2 import *


class PasswordApp(QMainWindow, PasswordUI):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.btn_start.setEnabled(False)
        self.lbl_sequence_n.setText('0')
        self.lbl_word_n.setText('0')
        self.lbl_digit_n.setText('0')
        self.lbl_letter_n.setText('0')
        self.lbl_length_n.setText('0')
        self.btn_open_password.clicked.connect(self.btn_clicked)
        self.btn_open_dict.clicked.connect(self.btn_clicked)
        self.btn_start.clicked.connect(self.btn_clicked)
        self.line_password.textChanged.connect(self.line_changed)
        self.line_dict.textChanged.connect(self.line_changed)

    def line_changed(self):
        if self.line_password.text() and self.line_dict.text():
            self.btn_start.setEnabled(True)
        else:
            self.btn_start.setEnabled(False)

    def btn_clicked(self):
        if self.sender() == self.btn_open_password:
            self.line_password.setText(QFileDialog.getOpenFileName()[0])
        elif self.sender() == self.btn_open_dict:
            self.line_dict.setText(QFileDialog.getOpenFileName()[0])
        elif self.sender() == self.btn_start:
            f = open(self.line_password.text(), 'r')
            passwords = f.readlines()
            f.close()
            passwords = list(map(lambda x: x[0: -1], passwords[0: -1])) + [passwords[-1]]
            f = open(self.line_dict.text(), 'r')
            dic = f.readlines()
            f.close()
            dic = list(map(lambda x: x[0: -1], dic[0: -1])) + [dic[-1]]

            for i in passwords:
                try:
                    assert check_size(i)
                except AssertionError:
                    self.lbl_length_n.setText(str(int(self.lbl_length_n.text()) + 1))
                try:
                    assert check_register(i)
                except AssertionError:
                    self.lbl_letter_n.setText(str(int(self.lbl_letter_n.text()) + 1))
                try:
                    assert check_numbers(i)
                except AssertionError:
                    self.lbl_digit_n.setText(str(int(self.lbl_digit_n.text()) + 1))
                try:
                    assert check_neighbors(i)
                except AssertionError:
                    self.lbl_sequence_n.setText(str(int(self.lbl_sequence_n.text()) + 1))
                try:
                    assert check_word(i, dic)
                except AssertionError:
                    self.lbl_word_n.setText(str(int(self.lbl_word_n.text()) + 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PasswordApp()
    w.show()
    sys.exit(app.exec())

