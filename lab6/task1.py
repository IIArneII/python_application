import csv
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtGui import QColor
from ui.task1_ui import Ui_MainWindow


class Task1App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.classes = set()
        self.schools = set()
        self.data = []
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.load_csv()
        self.list_class.currentTextChanged.connect(self.filter)
        self.list_school.currentTextChanged.connect(self.filter)

    def load_csv(self):
        f = open('ui/rez.csv', encoding="utf8")
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for i, row in enumerate(reader):
            if i != 0:
                self.schools.add(int(row[1][2:4]))
                self.classes.add(int(row[1][5:7]))
            self.data.append(row)
        self.schools = list(map(str, sorted(list(self.schools))))
        self.classes = list(map(str, sorted(list(self.classes))))
        self.list_school.addItem('Нет')
        self.list_class.addItem('Нет')
        self.list_school.addItems(self.schools)
        self.list_class.addItems(self.classes)

        self.update_table(self.data)

    def update_table(self, data):
        self.table.setColumnCount(3)
        d = [data[0][1], data[0][2], data[0][7]]
        self.table.setHorizontalHeaderLabels(d)
        self.table.setRowCount(0)
        if len(data) != 1:
            win = self.win(data)
            for i, row in enumerate(data[1:]):
                self.table.setRowCount(self.table.rowCount() + 1)
                for j, elem in enumerate(row):
                    if j in [1, 2, 7]:
                        self.table.setItem(i, [1, 2, 7].index(j), QTableWidgetItem(elem))
                        if i in win:
                            self.table.item(i, [1, 2, 7].index(j)).setBackground(QColor(0, 200, 200))
            self.table.resizeColumnsToContents()

    def filter(self):
        data = []
        if self.list_school.currentText() != 'Нет' or self.list_class.currentText() != 'Нет':
            for i, row in enumerate(self.data):
                if i == 0:
                    data.append(row)
                elif self.list_school.currentText() != 'Нет' and self.list_class.currentText() != 'Нет':
                    if int(row[1][2:4]) == int(self.list_school.currentText()) and int(row[1][5:7]) == int(
                            self.list_class.currentText()):
                        data.append(row)
                elif self.list_school.currentText() != 'Нет' and int(row[1][2:4]) == int(self.list_school.currentText()):
                    data.append(row)
                elif self.list_class.currentText() != 'Нет' and int(row[1][5:7]) == int(self.list_class.currentText()):
                    data.append(row)
            self.update_table(data)
        else:
            self.update_table(self.data)

    def win(self, data):

        d = [[int(row[-1]), i] for i, row in enumerate(data[1:])]

        max_i = []
        m = max(d, key=lambda x: x[0])
        max_i += [i[1] for i in d if i[0] == m[0]]
        d = [i for i in d if i[0] != m[0]]
        if d:
            m = max(d, key=lambda x: x[0])
            max_i += [i[1] for i in d if i[0] == m[0]]
            d = [i for i in d if i[0] != m[0]]
            if d:
                m = max(d, key=lambda x: x[0])
                max_i += [i[1] for i in d if i[0] == m[0]]
        return max_i


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task1App()
    w.show()
    sys.exit(app.exec())
