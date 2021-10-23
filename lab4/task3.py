import sys
import re
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from task1_ui import Ui_MainWindow


class NechChApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Задание 3')
        self.btn_start.clicked.connect(self.btn_clicked)
        self.btn_obz.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        if self.sender() == self.btn_obz:
            self.line_file.setText(QFileDialog.getOpenFileName()[0])
        if self.sender() == self.btn_start:
            try:
                f = open(self.line_file.text(), 'r')
                lines = f.readlines()
                f.close()
                lines = ''.join(lines)
                lines = np.array(list(map(int, re.findall('\d+', lines))))
                self.text_1.setText(
                    'min: ' + str(lines.min()) + '\nmax: ' + str(lines.max()) + '\nmean: ' + str(lines.mean()))
                f = open('output.txt', 'w')
                f.write(self.text_1.toPlainText())
                f.close()
            except:
                self.text_1.setText('Файл не найден')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = NechChApp()
    w.show()
    sys.exit(app.exec())
