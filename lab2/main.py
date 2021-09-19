import sys
import pickle
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.QtCore import QTime, QDate, Qt
from diary import Ui_Form


class DiaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
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
                'dd-MM-yyyy') + ' - ' + self.ui.time_line.text() + ' - Новое событие')
        self.ui.event_list.addItem(self.current_item)
        self.ui.name_line.setText('Новое событие')
        self.ui.name_line.selectAll()
        self.ui.name_line.setFocus()

        self.events[str(self.current_item)] = {'name': self.ui.name_line.text(), 'time': self.ui.time_line.text(),
                                               'note': self.ui.note_edit.toPlainText(),
                                               'date': self.ui.calendar.selectedDate().toString('dd-MM-yyyy')}

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

    def line_edited(self):
        if self.current_item:
            if self.sender() == self.ui.name_line:
                self.current_item.setText(self.ui.calendar.selectedDate().toString(
                    'dd-MM-yyyy') + ' - ' + self.ui.time_line.text() + ' - ' + self.ui.name_line.text())
                self.events[str(self.current_item)]['name'] = self.ui.name_line.text()
            elif self.sender() == self.ui.time_line:
                self.current_item.setText(self.ui.calendar.selectedDate().toString(
                    'dd-MM-yyyy') + ' - ' + self.ui.time_line.text() + ' - ' + self.ui.name_line.text())
                self.events[str(self.current_item)]['time'] = self.ui.time_line.text()
            elif self.sender() == self.ui.note_edit:
                self.events[str(self.current_item)]['note'] = self.ui.note_edit.toPlainText()
            elif self.sender() == self.ui.calendar:
                self.current_item.setText(self.ui.calendar.selectedDate().toString(
                    'dd-MM-yyyy') + ' - ' + self.ui.time_line.text() + ' - ' + self.ui.name_line.text())
                self.events[str(self.current_item)]['date'] = self.ui.calendar.selectedDate().toString('dd-MM-yyyy')
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
        self.ui.calendar.setSelectedDate(QDate.fromString(self.events[str(self.current_item)]['date'], 'dd-MM-yyyy'))

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
                self.events[str(self.current_item)] = {'name': i['name'], 'time': i['time'], 'note': i['time'],
                                                       'date': i['time']}
        f.close()
        self.ui.event_list.sortItems(Qt.AscendingOrder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DiaryApp()
    w.show()
    sys.exit(app.exec())
