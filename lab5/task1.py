from PIL import Image
from PIL.ImageQt import ImageQt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from ui.task1_ui import Ui_MainWindow

class Task1App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.image = None
        self.channel = None
        self.init_ui()

    def init_ui(self):
        file = QFileDialog.getOpenFileName(self, 'Выбрать изображение', '', 'Изображение (*.png);;Все файлы (*)')[0]
        if file:
            self.image = Image.open(file)
            self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))
            self.btn_red.clicked.connect(self.btn_clicked)
            self.btn_green.clicked.connect(self.btn_clicked)
            self.btn_blue.clicked.connect(self.btn_clicked)
            self.btn_left.clicked.connect(self.btn_clicked)
            self.btn_right.clicked.connect(self.btn_clicked)
        else:
            self.label.setText('Изображение не найдено')


    def btn_clicked(self):
        if self.sender() == self.btn_red:
            self.channel_r()
            self.channel = 'r'
        if self.sender() == self.btn_green:
            self.channel_g()
            self.channel = 'g'
        if self.sender() == self.btn_blue:
            self.channel_b()
            self.channel = 'b'
        if self.sender() == self.btn_left:
            self.image = self.image.rotate(90, expand=True)
            self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))
            if self.channel == 'r':
                self.channel_r()
            elif self.channel == 'g':
                self.channel_g()
            elif self.channel == 'b':
                self.channel_b()
        if self.sender() == self.btn_right:
            self.image = self.image.rotate(-90, expand=True)
            self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))
            if self.channel == 'r':
                self.channel_r()
            elif self.channel == 'g':
                self.channel_g()
            elif self.channel == 'b':
                self.channel_b()

    def channel_r(self):
        r, g, b = self.image.convert('RGB').split()
        g = g.point(lambda i: i * 0)
        b = b.point(lambda i: i * 0)
        result = Image.merge('RGB', (r, g, b)).convert("RGBA")
        self.label.setPixmap(QPixmap.fromImage(ImageQt(result)))

    def channel_g(self):
        r, g, b = self.image.convert('RGB').split()
        r = r.point(lambda i: i * 0)
        b = b.point(lambda i: i * 0)
        result = Image.merge('RGB', (r, g, b)).convert("RGBA")
        self.label.setPixmap(QPixmap.fromImage(ImageQt(result)))

    def channel_b(self):
        r, g, b = self.image.convert('RGB').split()
        g = g.point(lambda i: i * 0)
        r = r.point(lambda i: i * 0)
        result = Image.merge('RGB', (r, g, b)).convert("RGBA")
        self.label.setPixmap(QPixmap.fromImage(ImageQt(result)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task1App()
    w.show()
    sys.exit(app.exec())
