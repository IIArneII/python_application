# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.text_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit.setObjectName("text_edit")
        self.gridLayout.addWidget(self.text_edit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_new = QtWidgets.QAction(MainWindow)
        self.act_new.setObjectName("act_new")
        self.act_save = QtWidgets.QAction(MainWindow)
        self.act_save.setObjectName("act_save")
        self.act_save_as = QtWidgets.QAction(MainWindow)
        self.act_save_as.setObjectName("act_save_as")
        self.act_cancel = QtWidgets.QAction(MainWindow)
        self.act_cancel.setObjectName("act_cancel")
        self.act_repeat = QtWidgets.QAction(MainWindow)
        self.act_repeat.setObjectName("act_repeat")
        self.act_open = QtWidgets.QAction(MainWindow)
        self.act_open.setObjectName("act_open")
        self.act_save_as_ = QtWidgets.QAction(MainWindow)
        self.act_save_as_.setObjectName("act_save_as_")
        self.menu_file.addAction(self.act_new)
        self.menu_file.addAction(self.act_open)
        self.menu_file.addAction(self.act_save)
        self.menu_file.addAction(self.act_save_as_)
        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактор"))
        self.menu_file.setTitle(_translate("MainWindow", "Файл"))
        self.act_new.setText(_translate("MainWindow", "Новый"))
        self.act_save.setText(_translate("MainWindow", "Сохранить"))
        self.act_save_as.setText(_translate("MainWindow", "Сохранить как"))
        self.act_cancel.setText(_translate("MainWindow", "Отменить"))
        self.act_cancel.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.act_repeat.setText(_translate("MainWindow", "Повторить"))
        self.act_repeat.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.act_open.setText(_translate("MainWindow", "Открыть"))
        self.act_save_as_.setText(_translate("MainWindow", "Сохранить как"))
