import sys
import pickle
import re
import random
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMainWindow
from PyQt5.QtCore import QTime, QDate, Qt
from diary_ui import DiaryUI
from flags_ui import FlagsUI
from note_ui import NoteBookUI
from plagiarism_ui import PlagiarismUI
from stones_ui import StonesUI
from lab2_ui import Lab2UI


class Lab2App(QMainWindow, Lab2UI):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.w1 = FlagsApp()
        self.w2 = DiaryApp()
        self.w3 = NoteBookApp()
        self.w4 = StonesApp()
        self.w5 = PlagiarismApp()
        self.initUI()

    def initUI(self):
        self.task1.clicked.connect(self.btn_clicked)
        self.task2.clicked.connect(self.btn_clicked)
        self.task3.clicked.connect(self.btn_clicked)
        self.task4.clicked.connect(self.btn_clicked)
        self.task5.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        if self.sender() == self.task1:
            self.w1.show()
        if self.sender() == self.task2:
            self.w2.show()
        if self.sender() == self.task3:
            self.w3.show()
        if self.sender() == self.task4:
            self.w4.show()
        if self.sender() == self.task5:
            self.w5.show()


class FlagsApp(QWidget, FlagsUI):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.flags_check = [0, 0, 0]
        self.initUI()

    def initUI(self):
        self.btn.setText('Составить флаг')
        self.buttonGroup1.buttonClicked.connect(self.btns_clicked)
        self.buttonGroup2.buttonClicked.connect(self.btns_clicked)
        self.buttonGroup3.buttonClicked.connect(self.btns_clicked)
        self.btn.clicked.connect(self.draw)

    def btns_clicked(self, btn):
        if btn in self.buttonGroup1.buttons():
            self.flags_check[0] = btn.text()
        if btn in self.buttonGroup2.buttons():
            self.flags_check[1] = btn.text()
        if btn in self.buttonGroup3.buttons():
            self.flags_check[2] = btn.text()

    def draw(self):
        if 0 not in self.flags_check:
            self.label1.setText(self.flags_check[0])
            self.label2.setText(self.flags_check[1])
            self.label3.setText(self.flags_check[2])


class DiaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = DiaryUI()
        self.ui.setupUi(self)
        self.events = {}
        self.current_item = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Календарь')

        self.ui.add_btn.clicked.connect(self.add_btn_clicked)
        self.ui.name_line.textEdited.connect(self.line_edited)
        self.ui.time_line.timeChanged.connect(self.line_edited)
        self.ui.note_edit.textChanged.connect(self.line_edited)
        self.ui.calendar.selectionChanged.connect(self.line_edited)
        self.ui.event_list.itemClicked.connect(self.event_selection)
        self.ui.del_btn.clicked.connect(self.del_btn_clicked)
        self.data_load()

    def add_btn_clicked(self):
        if not self.current_item:
            self.ui.name_line.setEnabled(True)
            self.ui.time_line.setEnabled(True)
            self.ui.note_edit.setEnabled(True)

        self.current_item = QListWidgetItem(
            self.ui.calendar.selectedDate().toString(
                'yyyy-MM--dd') + ' - ' + self.ui.time_line.text() + ' - Новое событие')
        self.ui.event_list.addItem(self.current_item)
        self.ui.name_line.setText('Новое событие')
        self.ui.name_line.selectAll()
        self.ui.name_line.setFocus()

        self.events[str(self.current_item)] = {'name': self.ui.name_line.text(), 'time': self.ui.time_line.text(),
                                               'note': self.ui.note_edit.toPlainText(),
                                               'date': self.ui.calendar.selectedDate().toString('yyyy-MM--dd')}

        self.ui.note_edit.clear()
        self.ui.time_line.setTime(QTime(0, 0))
        self.ui.event_list.sortItems(Qt.AscendingOrder)
        self.data_dump()

    def del_btn_clicked(self):
        if self.current_item and self.ui.event_list.currentRow() != -1:
            take = self.ui.event_list.takeItem(self.ui.event_list.currentRow())
            del self.events[str(take)]
            if self.ui.event_list.currentRow() != -1:
                self.event_selection()
                self.ui.event_list.sortItems(Qt.AscendingOrder)
            else:
                self.current_item = None
                self.ui.name_line.setEnabled(False)
                self.ui.time_line.setEnabled(False)
                self.ui.note_edit.setEnabled(False)
                self.ui.note_edit.clear()
                self.ui.time_line.setTime(QTime(0, 0))
                self.data_dump()

    def line_edited(self):
        if self.current_item:
            if self.sender() == self.ui.name_line:
                self.current_item.setText(self.ui.calendar.selectedDate().toString(
                    'yyyy-MM--dd') + ' - ' + self.ui.time_line.text() + ' - ' + self.ui.name_line.text())
                self.events[str(self.current_item)]['name'] = self.ui.name_line.text()
            elif self.sender() == self.ui.time_line:
                self.current_item.setText(self.ui.calendar.selectedDate().toString(
                    'yyyy-MM--dd') + ' - ' + self.ui.time_line.text() + ' - ' + self.ui.name_line.text())
                self.events[str(self.current_item)]['time'] = self.ui.time_line.text()
            elif self.sender() == self.ui.note_edit:
                self.events[str(self.current_item)]['note'] = self.ui.note_edit.toPlainText()
            elif self.sender() == self.ui.calendar:
                self.current_item.setText(self.ui.calendar.selectedDate().toString(
                    'yyyy-MM--dd') + ' - ' + self.ui.time_line.text() + ' - ' + self.ui.name_line.text())
                self.events[str(self.current_item)]['date'] = self.ui.calendar.selectedDate().toString('yyyy-MM--dd')
            self.ui.event_list.sortItems(Qt.AscendingOrder)
            self.data_dump()

    def event_selection(self):
        self.ui.name_line.setEnabled(True)
        self.ui.time_line.setEnabled(True)
        self.ui.note_edit.setEnabled(True)
        self.current_item = self.ui.event_list.currentItem()
        self.ui.name_line.setText(self.events[str(self.current_item)]['name'])
        self.ui.time_line.setTime(QTime(QTime.fromString(self.events[str(self.current_item)]['time'], 'h:mm')))
        self.ui.note_edit.setPlainText(self.events[str(self.current_item)]['note'])
        self.ui.calendar.setSelectedDate(QDate.fromString(self.events[str(self.current_item)]['date'], 'yyyy-MM--dd'))

    def data_dump(self):
        f = open('data.pickle', 'wb')
        pickle.dump(list(self.events.values()), f)
        f.close()

    def data_load(self):
        f = open('data.pickle', 'rb')
        data = pickle.load(f)
        if data:
            for i in data:
                self.current_item = QListWidgetItem(
                    i['date'] + ' - ' + i['time'] + ' - ' + i['name'])
                self.ui.event_list.addItem(self.current_item)
                self.events[str(self.current_item)] = {'name': i['name'], 'time': i['time'], 'note': i['note'],
                                                       'date': i['date']}
        f.close()
        self.ui.event_list.sortItems(Qt.AscendingOrder)


class NoteBookApp(QMainWindow, NoteBookUI):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.current_item = None
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_del.clicked.connect(self.btn_clicked)
        self.list.itemClicked.connect(self.item_selection)
        self.name_edit.textEdited.connect(self.line_edited)
        self.phone_edit.textEdited.connect(self.line_edited)

    def btn_clicked(self):
        if self.sender() == self.btn_add:
            self.current_item = QListWidgetItem(self.name_edit.text() + ': ' + self.phone_edit.text())
            self.list.addItem(self.current_item)

            self.name_edit.clear()
            self.phone_edit.clear()
            self.btn_add.setEnabled(False)
        if self.sender() == self.btn_del:
            self.list.takeItem(self.list.currentRow())

            self.current_item = self.list.currentItem()

            if self.list.currentRow() != -1:
                self.item_selection()
            else:
                self.current_item = None
                self.btn_del.setEnabled(False)

    def line_edited(self):
        if self.name_edit.text() and self.phone_edit.text() and self.phone_edit.text().isdigit():
            self.btn_add.setEnabled(True)
        else:
            self.btn_add.setEnabled(False)

    def item_selection(self):
        self.current_item = self.list.currentItem()
        self.btn_del.setEnabled(True)


class StonesApp(QMainWindow, StonesUI):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.count = 0;
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Псевдоним')
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)
        self.btn1.clicked.connect(self.btn_clicked)
        self.btn2.clicked.connect(self.btn_clicked)
        self.btn3.clicked.connect(self.btn_clicked)
        self.btn_new_game.clicked.connect(self.btn_new_game_clicked)

    def btn_clicked(self):
        if self.sender() == self.btn1:
            self.count -= 1
            self.add_history(f'---Вы забрали 1. Камней: {self.count}')
        if self.sender() == self.btn2:
            self.count -= 2
            self.add_history(f'---Вы забрали 2. Камней: {self.count}')
        if self.sender() == self.btn3:
            self.count -= 3
            self.add_history(f'---Вы забрали 3. Камней: {self.count}')

        if self.count % 4 != 0:
            self.add_history(f'==ИИ забрал {self.count % 4}. Камней: {self.count - self.count % 4}')
            self.count -= self.count % 4
            if self.count == 0:
                self.add_history(f'-=-=-=ИИ Выиграл=-=-=-')
                self.game_indicate_label.setText('ИИ Выиграл')
                self.btn1.setEnabled(False)
                self.btn2.setEnabled(False)
                self.btn3.setEnabled(False)
        else:
            if self.count != 0:
                r = random.randint(1, 3)
                self.count -= r
                self.add_history(f'==ИИ забрал {r}. Камней: {self.count}')
            else:
                self.add_history(f'-=-=-=Вы Выиграли=-=-=-')
                self.game_indicate_label.setText('Вы Выиграли')
                self.btn1.setEnabled(False)
                self.btn2.setEnabled(False)
                self.btn3.setEnabled(False)

        if self.count == 1:
            self.btn2.setEnabled(False)
            self.btn3.setEnabled(False)
        elif self.count == 2:
            self.btn3.setEnabled(False)
        if self.count != 0:
            self.game_indicate_label.setText(str(self.count))

    def btn_new_game_clicked(self):
        self.game_indicate_label.setText(self.stones_count.text())
        self.add_history('-=-=-=-=-=-=-=-=-=-=-=-\nНовая игра. Камней: ' + self.stones_count.text())
        self.count = int(self.stones_count.text())
        if self.count == 1:
            self.btn2.setEnabled(False)
            self.btn3.setEnabled(False)
        elif self.count == 2:
            self.btn3.setEnabled(False)
        elif self.count > 2:
            self.btn1.setEnabled(True)
            self.btn2.setEnabled(True)
            self.btn3.setEnabled(True)

    def add_history(self, text):
        self.history.setText(self.history.toPlainText() + '\n' + text)


class PlagiarismApp(QMainWindow, PlagiarismUI):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Антиплагиат')
        self.btn.clicked.connect(self.plagiarism)
        self.edit1.textChanged.connect(self.text_edited)
        self.edit2.textChanged.connect(self.text_edited)

    def text_edited(self):
        if self.edit1.toPlainText() and self.edit2.toPlainText():
            self.btn.setEnabled(True)
        else:
            self.btn.setEnabled(False)

    def plagiarism(self):
        text1 = re.sub('[^А-Яа-яA-Za-z ]', '', self.edit1.toPlainText()).lower()
        text2 = re.sub('[^А-Яа-яA-Za-z ]', '', self.edit2.toPlainText()).lower()
        text1 = self.pair_up(text1)
        text2 = self.pair_up(text2)
        self.supplement(text1, text2)
        uniqueness = 0
        max_uniqueness = 0
        for key in text1:
            uniqueness += abs(text1[key] - text2[key])
            max_uniqueness += text1[key] + text2[key]
        uniqueness = (uniqueness / max_uniqueness) ** (self.slider.value() / 100) * 100
        self.progress.setValue(int(uniqueness))

    def pair_up(self, text):
        text1 = text.split()
        d1 = {}
        if len(text1) > 1:
            for i in range(len(text1) - 1):
                temp1 = ' '.join(text1[i: i + 2])
                temp2 = ' '.join(text1[i: i + 2][::-1])
                if temp1 not in d1:
                    d1[temp1] = 1
                    d1[temp2] = 1
                else:
                    d1[temp1] += 1
                    d1[temp2] += 1
        else:
            d1[text1[0]] = 1
        return d1

    def supplement(self, d1, d2, val=0):
        for key in d2:
            if key not in d1:
                d1[key] = val
        for key in d1:
            if key not in d2:
                d2[key] = val


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Lab2App()
    w.show()
    sys.exit(app.exec())
