import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLayoutItem
from PyQt5.QtCore import QSettings, QCoreApplication
from PyQt5 import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent
from ui.task3_ui import Ui_MainWindow


class Text(QTextBrowser):
    def __init__(self, parent):
        super(Text, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e: QDragMoveEvent) -> None:
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QDropEvent) -> None:
        if e.mimeData().text()[0: 8] == 'file:///':
            url = e.mimeData().text()[8:]
            f = open(url, 'r', encoding='utf-8')
            self.setText(''.join(f.readlines()))
            f.close()
        else:
            self.setText(e.mimeData().text())


class Task3App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Task3App, self).__init__()
        self.text = Text(self)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.gridLayout.addWidget(self.text, 0, 0)
        self.setAcceptDrops(True)
        self.text.setAcceptDrops(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task3App()
    w.show()
    sys.exit(app.exec())
