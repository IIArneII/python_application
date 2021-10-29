import random
from PIL import Image
from PIL.ImageQt import ImageQt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from ui.task2_ui import Ui_MainWindow


class Task2App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.image = None
        self.init_ui()

    def init_ui(self):
        file = QFileDialog.getOpenFileName(self, 'Выбрать изображение', '', 'Изображение (*.png);;Все файлы (*)')[0]
        if file:
            self.image = Image.open(file)
            self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))

            self.slider.valueChanged.connect(self.slider_changed)
        else:
            self.label.setText('Изображение не найдено')

    def slider_changed(self):
        r, g, b, a = self.image.split()
        a = a.point(lambda i: self.slider.value())
        result = Image.merge('RGBA', (r, g, b, a))
        self.label.setPixmap(QPixmap.fromImage(ImageQt(result)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task2App()
    w.show()
    sys.exit(app.exec())