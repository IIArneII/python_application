import sys
import re
from PyQt5.QtGui import QPainter, QColor, QPaintEvent, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QMainWindow, QFileDialog
from PyQt5.QtCore import QPoint, QRectF
from ui.task7_ui import Ui_MainWindow


class LSystem:
    def __init__(self):
        self.axioms = ''
        self.theorems = {}

    def get_system(self, n):
        line1 = self.axioms
        for i in range(n):
            line2 = ''
            for j in line1:
                if j in self.theorems:
                    line2 += self.theorems[j]
                elif j in ['+', '-', '[', ']']:
                    line2 += j
            line1 = line2
        return line1


class Task7App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.l_system = LSystem()
        self.true_draw = False
        self.pen = QPen()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.line_aks.setText('A')
        self.line_teo1.setText('A=A-A++A-A')
        self.slider_angle.setValue(60)
        self.slider_iter.setValue(4)

        self.pen.setColor(QColor(0, 0, 0))
        self.slider_iter.valueChanged.connect(self.slider_value_changed)
        self.slider_angle.valueChanged.connect(self.slider_value_changed)
        self.slider_x.valueChanged.connect(self.slider_value_changed)
        self.slider_y.valueChanged.connect(self.slider_value_changed)
        self.slider_l.valueChanged.connect(self.slider_value_changed)
        self.line_teo1.textChanged.connect(self.l_system_chang)
        self.line_teo2.textChanged.connect(self.l_system_chang)
        self.line_teo3.textChanged.connect(self.l_system_chang)
        self.line_aks.textChanged.connect(self.l_system_chang)
        self.btn.clicked.connect(self.btn_clicked)

        self.l_system_chang()

    def btn_clicked(self):
        file = QFileDialog.getOpenFileName()[0]
        if file:
            f = open(file, 'r')
            lines = f.readlines()
            f.close()
            lines = list(map(lambda x: re.sub('\n', '', x), lines))
            print(lines)
            self.setWindowTitle(lines[0])
            self.slider_angle.setValue(int(lines[1]))
            self.line_aks.setText(lines[2])
            if len(lines) > 3:
                self.line_teo1.setText(lines[3])
            if len(lines) > 4:
                self.line_teo2.setText(lines[4])
            if len(lines) > 5:
                self.line_teo3.setText(lines[5])

    def l_system_chang(self):
        try:
            self.l_system.theorems.clear()
            if self.line_teo1.text():
                l = self.line_teo1.text().split('=')
                self.l_system.theorems[l[0]] = l[1]
            if self.line_teo2.text():
                l = self.line_teo2.text().split('=')
                self.l_system.theorems[l[0]] = l[1]
            if self.line_teo3.text():
                l = self.line_teo3.text().split('=')
                self.l_system.theorems[l[0]] = l[1]
            if self.line_aks.text():
                self.l_system.axioms = self.line_aks.text()
                self.label.clear()
                self.true_draw = True
                self.update()
            else:
                self.true_draw = False
                self.label.setText('Вы не ввели аксиому...')
        except:
            self.true_draw = False
            self.label.setText('Вы ввели что то не то...')

    def slider_value_changed(self):
        self.lbl_info.setText(
            f'Угол: {self.slider_angle.value()}    Итерация: {self.slider_iter.value()}    Длина: {self.slider_l.value()}')
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setPen(self.pen)
        p.translate(int(20 + self.slider_x.value() * self.width() / 100),
                    int(self.slider_y.value() * self.height() / 100))
        p.rotate(180 + self.slider_angle.value())
        p.begin(self)
        if self.true_draw:
            self.draw(p)
        p.end()

    def draw(self, p):
        line = self.l_system.get_system(self.slider_iter.value())
        for i in line:
            if i == '-':
                p.rotate(-self.slider_angle.value())
            elif i == '+':
                p.rotate(self.slider_angle.value())
            elif i == '[':
                p.save()
            elif i == ']':
                p.restore()
            else:
                p.drawLine(0, 0, 0, int(self.slider_l.value() / self.slider_iter.value()))
                p.translate(0, int(self.slider_l.value() / self.slider_iter.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Task7App()
    ex.show()
    sys.exit(app.exec())
