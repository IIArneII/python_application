# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_school = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_school.sizePolicy().hasHeightForWidth())
        self.lbl_school.setSizePolicy(sizePolicy)
        self.lbl_school.setObjectName("lbl_school")
        self.gridLayout.addWidget(self.lbl_school, 0, 0, 1, 1)
        self.list_school = QtWidgets.QComboBox(self.centralwidget)
        self.list_school.setObjectName("list_school")
        self.gridLayout.addWidget(self.list_school, 0, 1, 1, 1)
        self.lbl_class = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_class.sizePolicy().hasHeightForWidth())
        self.lbl_class.setSizePolicy(sizePolicy)
        self.lbl_class.setObjectName("lbl_class")
        self.gridLayout.addWidget(self.lbl_class, 1, 0, 1, 1)
        self.list_class = QtWidgets.QComboBox(self.centralwidget)
        self.list_class.setObjectName("list_class")
        self.gridLayout.addWidget(self.list_class, 1, 1, 1, 1)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout.addWidget(self.table, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_school.setText(_translate("MainWindow", "Школа"))
        self.lbl_class.setText(_translate("MainWindow", "Класс"))
