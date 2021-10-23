import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from task4_ui import Ui_MainWindow


class TextEditApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.current_file = ''
        self.init_ui()

    def init_ui(self):
        self.text_edit.cursorPositionChanged.connect(self.cursor_changed)
        self.act_new.triggered.connect(self.new_file)
        self.act_save.triggered.connect(self.save_file)
        self.act_open.triggered.connect(self.open_file)
        self.act_save_as_.triggered.connect(self.save_as_file)

    def cursor_changed(self):
        self.statusbar.showMessage(
            str(self.text_edit.textCursor().blockNumber()) + ':' + str(self.text_edit.textCursor().positionInBlock()))

    def open_file(self):
        self.current_file = QFileDialog.getOpenFileName()[0]
        if self.current_file != '':
            f = open(self.current_file, 'r')
            lines = f.readlines()
            f.close()
            lines = ''.join(lines)
            self.text_edit.setPlainText(lines)

    def save_file(self):
        if self.current_file != '':
            f = open(self.current_file, 'w')
            f.write(self.text_edit.toPlainText())
            f.close()
        else:
            self.save_as_file()

    def save_as_file(self):
        self.current_file = QFileDialog.getSaveFileName()[0]
        if self.current_file != '':
            f = open(self.current_file, 'w')
            f.write(self.text_edit.toPlainText())
            f.close()

    def new_file(self):
        self.current_file = ''
        self.text_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TextEditApp()
    w.show()
    sys.exit(app.exec())
