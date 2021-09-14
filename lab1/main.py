import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QCheckBox, QLabel, QTextEdit, QPlainTextEdit


class Lab1(QWidget):
    def __init__(self):
        super().__init__()

        self.task1 = QPushButton('Задание 1', self)
        self.task2 = QPushButton('Задание 2', self)
        self.task3 = QPushButton('Задание 3', self)
        self.task4 = QPushButton('Задание 4', self)
        self.task5 = QPushButton('Задание 5', self)
        self.task6 = QPushButton('Задание 6', self)
        self.label = QLabel('Лабораторная 1\nШванев Арсений', self)

        self.w_task1 = Task1()
        self.w_task2 = Task2()
        self.w_task3 = Task3()
        self.w_task4 = Task4()
        self.w_task5 = Task5()

        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 200, 300)
        self.setWindowTitle('Лабраторная 1 - Шванев Арсений')

        self.task1.move(60, 20)
        self.task2.move(60, 60)
        self.task3.move(60, 100)
        self.task4.move(60, 140)
        self.task5.move(60, 180)
        self.task6.move(60, 220)
        self.label.move(60, 260)

        self.task6.setEnabled(False)

        self.task1.clicked.connect(self.btn_pressed)
        self.task2.clicked.connect(self.btn_pressed)
        self.task3.clicked.connect(self.btn_pressed)
        self.task4.clicked.connect(self.btn_pressed)
        self.task5.clicked.connect(self.btn_pressed)
        self.task6.clicked.connect(self.btn_pressed)

    def btn_pressed(self):
        if self.sender() == self.task1:
            self.w_task1.show()
        if self.sender() == self.task2:
            self.w_task2.show()
        if self.sender() == self.task3:
            self.w_task3.show()
        if self.sender() == self.task4:
            self.w_task4.show()
        if self.sender() == self.task5:
            self.w_task5.show()


class Task1(QWidget):
    def __init__(self):
        super().__init__()

        self.line1 = QLineEdit('перекидыватель', self)
        self.line2 = QLineEdit(self)
        self.btn = QPushButton('--->', self)

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 500, 100)
        self.setWindowTitle('Задание 1')

        self.line1.move(50, 40)
        self.line2.move(300, 40)
        self.btn.move(200, 40)

        self.btn.clicked.connect(self.btn_move)

    def btn_move(self):
        if self.btn.text() == '--->':
            self.btn.setText('<---')
            self.line2.setText(self.line1.text())
            self.line1.clear()
        else:
            self.btn.setText('--->')
            self.line1.setText(self.line2.text())
            self.line2.clear()


class Task2(QWidget):
    def __init__(self):
        super().__init__()

        self.line1 = QLineEdit(self)
        self.line2 = QLineEdit(self)
        self.btn = QPushButton('Вычислить', self)

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 500, 100)
        self.setWindowTitle('Задание 2')

        self.line1.move(50, 40)
        self.line2.move(300, 40)
        self.btn.move(200, 40)

        self.btn.clicked.connect(self.btn_pressed)

    def btn_pressed(self):
        if self.line1.text() == '':
            self.line2.setText('Вы ничего не ввели')
        else:
            self.line2.setText(str(eval(self.line1.text())))


class Task3(QWidget):
    def __init__(self):
        super().__init__()

        self.chb1 = QCheckBox(self)
        self.chb2 = QCheckBox(self)
        self.chb3 = QCheckBox(self)

        self.btn = QPushButton('Кнопка', self)
        self.line = QLineEdit('Строка для ввода', self)
        self.label = QLabel('Бирка', self)

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 200, 100)
        self.setWindowTitle('Задание 3')

        self.chb1.move(20, 20)
        self.chb2.move(20, 50)
        self.chb3.move(20, 80)
        self.btn.move(50, 20)
        self.line.move(50, 50)
        self.label.move(50, 80)

        self.chb1.clicked.connect(self.chb_pressed)
        self.chb2.clicked.connect(self.chb_pressed)
        self.chb3.clicked.connect(self.chb_pressed)

    def chb_pressed(self):
        if self.chb1 == self.sender():
            self.btn.setVisible(not self.btn.isVisible())
        if self.chb2 == self.sender():
            self.line.setVisible(not self.line.isVisible())
        if self.chb3 == self.sender():
            self.label.setVisible(not self.label.isVisible())


class Task4(QWidget):
    def __init__(self):
        super().__init__()

        self.alphabet = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•',
                         'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•',
                         'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—',
                         'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}

        self.btns = [QPushButton(i[0], self) for i in self.alphabet.items()]
        self.text = QTextEdit(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 200, 400, 800)
        self.setWindowTitle('Задание 4')

        self.text.move(120, 70)

        h = 10
        for i in self.btns:
            i.move(10, h)
            i.clicked.connect(self.btn_pressed)
            h += 30

    def btn_pressed(self):
        for i in self.btns:
            if self.sender() == i:
                self.text.setText(self.text.toPlainText() + ' ' + self.alphabet[i.text()])


class Task5(QWidget):
    def __init__(self):
        super().__init__()

        self.menu = {'Суши': [1000, 0], 'Блины': [200, 0], 'Кекс': [300, 0]}
        self.text = QPlainTextEdit(self)
        self.ui = []
        for i in self.menu.items():
            self.ui.append([QLabel(i[0], self), QPushButton('+', self), QPushButton('-', self)])

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 400, 400)
        self.setWindowTitle('Задание 5')

        h = 10
        for i in self.ui:
            i[0].move(10, h)
            i[1].move(80, h)
            i[2].move(200, h)
            i[1].clicked.connect(self.btn_pressed)
            i[2].clicked.connect(self.btn_pressed)
            h += 30

        self.text.move(10, h)
        self.change_receipt()

    def btn_pressed(self):
        for i in self.ui:
            if i[1] == self.sender():
                self.menu[i[0].text()][1] += 1
            elif i[2] == self.sender() and self.menu[i[0].text()][1] > 0:
                self.menu[i[0].text()][1] -= 1
        self.change_receipt()

    def change_receipt(self):
        s = 0
        line = '\tЧЕК\n\nБлюдо\tЦена\tИтого\n\n'
        for i in self.menu.items():
            if i[1][1] > 0:
                line = line + i[0] + '\t' + str(i[1][0]) + ' * ' + str(i[1][1]) + '\t' + str(i[1][0] * i[1][1]) + '\n'
                s += i[1][0] * i[1][1]
        line = line + '\nИтого\t' + str(s)
        self.text.setPlainText(line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Lab1()
    w.show()
    sys.exit(app.exec())
