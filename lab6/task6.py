import sys
import re
import hashlib
import secrets
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ui.task6_ui import Ui_MainWindow
from ui.task6_dialog_ui import Ui_Dialog


def check_password(password):
    lit = {
        'й': 1, 'ц': 2, 'у': 3, 'к': 4, 'е': 5, 'н': 6, 'г': 7, 'ш': 8, 'щ': 9, 'з': 10, 'х': 11, 'ъ': 12,
        'ф': 14, 'ы': 15, 'в': 16, 'а': 17, 'п': 18, 'р': 19, 'о': 20, 'л': 21, 'д': 22, 'ж': 23, 'э': 24, 'ё': 25,
        'я': 27, 'ч': 28, 'с': 29, 'м': 30, 'и': 31, 'т': 32, 'ь': 33, 'б': 34, 'ю': 35,
        'q': 41, 'w': 42, 'e': 43, 'r': 44, 't': 45, 'y': 46, 'u': 47, 'i': 48, 'o': 49, 'p': 50,
        'a': 54, 's': 55, 'd': 56, 'f': 57, 'g': 58, 'h': 59, 'j': 60, 'k': 61, 'l': 62,
        'z': 67, 'x': 68, 'c': 69, 'v': 70, 'b': 71, 'n': 72, 'm': 73
    }

    if len(password) < 8:
        return 'Длина пароля должна быть не менее 8 символов'
    if not re.findall('\d', password):
        return 'Пароль должен содержать хотя бы одну цифру'
    if not re.findall('[A-ZА-Я]', password) or not re.findall('[a-zа-я]', password):
        return 'Пароль должен содержать буквы обоих регистров'
    pas = [password[i: i + 3].lower() for i in range(len(password) - 2)]
    for i in pas:
        if not re.findall('[^a-zа-я]', i):
            if lit[i[1]] - lit[i[0]] == 1 and lit[i[2]] - lit[i[1]] == 1:
                return 'Обнаружена тройка соседних на клавиатуре букв'
    return True


def get_hash_password(password):
    salt = secrets.randbits(256).to_bytes(32, 'big')
    h = hashlib.scrypt(password, salt=salt, n=8, r=256, p=4, dklen=32)
    return h, salt


def check_hash_password(password, hash, salt):
    h = hashlib.scrypt(password, salt=salt, n=8, r=256, p=4, dklen=32)
    return hash == h


class Task6Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.mode = 'close'
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.btn_cancel.clicked.connect(self.btn_clicked)
        self.btn_register.clicked.connect(self.btn_clicked)
        self.btn_login.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        if self.sender() == self.btn_cancel:
            self.close()
        elif self.sender() == self.btn_login:
            if self.line_login.text() != '' and self.line_password.text() != '':
                self.mode = 'login'
                self.close()
        elif self.sender() == self.btn_register:
            if self.line_login.text() != '' and self.line_password.text() != '':
                self.mode = 'register'
                self.close()

    @staticmethod
    def get_login_data(login='', info=''):
        dialog = Task6Dialog()
        dialog.line_login.setText('admin')
        dialog.line_password.setText('Admin123')
        dialog.lbl_info.setText(info)
        if login != '':
            dialog.line_password.setFocus()
        dialog.exec_()
        return dialog.mode, dialog.line_login.text(), dialog.line_password.text()


class Task6App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.db = sqlite3.connect('db_library.db3')
        self.db_cursor = self.db.cursor()
        self.authorization = False
        self.add_rows = 0
        self.add_data = {}
        self.del_data = []
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.login()
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_del.clicked.connect(self.btn_clicked)
        self.btn_save.clicked.connect(self.btn_clicked)
        self.btn_find.clicked.connect(self.btn_clicked)
        self.table.itemChanged.connect(self.item_changed)
        self.load_data()

    def btn_clicked(self):
        if self.sender() == self.btn_find:
            self.load_data()
        elif self.sender() == self.btn_save:
            self.add_rows = 0
            self.save_data()
            self.add_data = {}
        elif self.sender() == self.btn_add:
            self.table.setRowCount(self.table.rowCount() + 1)
            self.add_rows += 1
            result = self.db_cursor.execute("""SELECT id FROM books ORDER BY id""").fetchall()
            if result:
                free = (result[-1][0] + self.add_rows)
            else:
                free = self.add_rows
            item = QTableWidgetItem(str(free))
            item.setFlags(Qt.ItemIsEnabled)
            pix = QPixmap('img/0.jpg')
            img = QTableWidgetItem()
            img.setData(Qt.DecorationRole, pix)
            self.table.itemChanged.disconnect(self.item_changed)
            self.table.setItem(self.table.rowCount() - 1, 1, item)
            self.table.setItem(self.table.rowCount() - 1, 0, img)
            self.table.itemChanged.connect(self.item_changed)
            self.add_data[str(free)] = {}
            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()
        elif self.sender() == self.btn_del:
            self.del_data.append(self.table.item(self.table.currentRow(), 1).text())
            self.table.removeRow(self.table.currentRow())
            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()

    def item_changed(self, item: QTableWidgetItem):
        if self.table.item(item.row(), 1).text() not in self.add_data:
            self.add_data[self.table.item(item.row(), 1).text()] = {}
        self.add_data[self.table.item(item.row(), 1).text()][
            self.table.horizontalHeaderItem(item.column()).text()] = item.text()
        if item.column() == 4:
            pix = QPixmap(item.text())
            if item.text() == '':
                pix = QPixmap('img/0.jpg')
            img = QTableWidgetItem()
            img.setData(Qt.DecorationRole, pix)
            self.table.setItem(item.row(), 0, img)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def save_data(self):
        if self.add_data:
            for id, data in self.add_data.items():
                if len(self.db_cursor.execute(f'SELECT 1 FROM books WHERE id = {id}').fetchall()) == 0:
                    sql = f"INSERT INTO books (id, name, author, url_image) VALUES( {id}, '', '', '')"
                    self.db_cursor.execute(sql)
                sql = 'UPDATE books SET\n' + ', '.join(
                    [f"{key} = '{item}'" for key, item in data.items() if key != 'img']) + f'\nWHERE id = {id}'
                if data != {}:
                    self.db_cursor.execute(sql)
        if self.del_data:
            for id in self.del_data:
                sql = f"DELETE FROM books WHERE id = {id}"
                self.db_cursor.execute(sql)
        self.db.commit()

    def load_data(self):
        self.table.itemChanged.disconnect(self.item_changed)
        result = self.db_cursor.execute(f"""SELECT * FROM books
                                            WHERE name LIKE '%{self.line_name.text()}%'
                                            AND author LIKE '%{self.line_author.text()}%'
                                            ORDER BY name""").fetchall()
        title = self.db_cursor.execute('PRAGMA table_info(books)')
        title = ['img'] + [i[1] for i in title]

        self.table.setColumnCount(len(title))
        self.table.setRowCount(len(result))
        self.table.setHorizontalHeaderLabels(title)
        for i, row in enumerate(result):
            pix = QPixmap(row[3])
            if row[3] == '':
                pix = QPixmap('img/0.jpg')
            img = QTableWidgetItem()
            img.setData(Qt.DecorationRole, pix)
            self.table.setItem(i, 0, img)
            for j, item in enumerate(row):
                if item != None:
                    self.table.setItem(i, j + 1, QTableWidgetItem(str(item)))
                if j == 0:
                    self.table.item(i, 1).setFlags(Qt.ItemIsEnabled)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.itemChanged.connect(self.item_changed)

    def login(self):
        log = ''
        info = ''
        l = ('',)
        while l[0] != 'close':
            l = Task6Dialog.get_login_data(log, info)
            if l[0] == 'login':
                result = self.db_cursor.execute(f"SELECT * FROM users WHERE login = '{l[1]}'").fetchall()
                if len(result) != 0:
                    if check_hash_password(l[2].encode(), bytes.fromhex(result[0][1]), bytes.fromhex(result[0][2])):
                        self.authorization = True
                        break
                    else:
                        log = l[1]
                        info = 'Неаверный пароль'
                else:
                    log = l[1]
                    info = 'Неверный логин'
            if l[0] == 'register':
                if type(check_password(l[2])) == str:
                    log = l[1]
                    info = check_password(l[2])
                else:
                    result = self.db_cursor.execute(f"SELECT * FROM users WHERE login = '{l[1]}'").fetchall()
                    if len(result) == 0:
                        h, salt = get_hash_password(l[2].encode())
                        self.db_cursor.execute(f"INSERT INTO users VALUES ('{l[1]}', '{h.hex()}', '{salt.hex()}')")
                        self.db.commit()
                        log = l[1]
                        info = 'Войдите в созданный аккаунт'
                    else:
                        log = l[1]
                        info = 'Этот пользователь уже существует'

    def closeEvent(self, e):
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Task6App()
    if w.authorization:
        w.show()
        sys.exit(app.exec())
