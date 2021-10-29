# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task7.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1154, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.slider_x = QtWidgets.QSlider(self.centralwidget)
        self.slider_x.setProperty("value", 50)
        self.slider_x.setOrientation(QtCore.Qt.Horizontal)
        self.slider_x.setObjectName("slider_x")
        self.gridLayout.addWidget(self.slider_x, 0, 0, 1, 7)
        self.line_teo1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_teo1.setObjectName("line_teo1")
        self.gridLayout.addWidget(self.line_teo1, 9, 2, 1, 1)
        self.slider_y = QtWidgets.QSlider(self.centralwidget)
        self.slider_y.setProperty("value", 50)
        self.slider_y.setOrientation(QtCore.Qt.Vertical)
        self.slider_y.setInvertedAppearance(True)
        self.slider_y.setObjectName("slider_y")
        self.gridLayout.addWidget(self.slider_y, 1, 0, 11, 1)
        self.slider_angle = QtWidgets.QSlider(self.centralwidget)
        self.slider_angle.setMinimum(-180)
        self.slider_angle.setMaximum(180)
        self.slider_angle.setOrientation(QtCore.Qt.Horizontal)
        self.slider_angle.setObjectName("slider_angle")
        self.gridLayout.addWidget(self.slider_angle, 9, 4, 1, 3)
        self.line_teo2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_teo2.setObjectName("line_teo2")
        self.gridLayout.addWidget(self.line_teo2, 10, 2, 1, 1)
        self.line_teo3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_teo3.setObjectName("line_teo3")
        self.gridLayout.addWidget(self.line_teo3, 11, 2, 1, 1)
        self.lbl_angle = QtWidgets.QLabel(self.centralwidget)
        self.lbl_angle.setObjectName("lbl_angle")
        self.gridLayout.addWidget(self.lbl_angle, 9, 3, 1, 1)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.gridLayout.addWidget(self.btn, 11, 3, 1, 4)
        self.lbl_info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_info.setObjectName("lbl_info")
        self.gridLayout.addWidget(self.lbl_info, 10, 3, 1, 4)
        self.lbl_teo3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_teo3.setObjectName("lbl_teo3")
        self.gridLayout.addWidget(self.lbl_teo3, 11, 1, 1, 1)
        self.lbl_teo2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_teo2.setObjectName("lbl_teo2")
        self.gridLayout.addWidget(self.lbl_teo2, 10, 1, 1, 1)
        self.lbl_teo1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_teo1.setObjectName("lbl_teo1")
        self.gridLayout.addWidget(self.lbl_teo1, 9, 1, 1, 1)
        self.lbl_aks = QtWidgets.QLabel(self.centralwidget)
        self.lbl_aks.setObjectName("lbl_aks")
        self.gridLayout.addWidget(self.lbl_aks, 8, 1, 1, 1)
        self.line_aks = QtWidgets.QLineEdit(self.centralwidget)
        self.line_aks.setObjectName("line_aks")
        self.gridLayout.addWidget(self.line_aks, 8, 2, 1, 1)
        self.lbl_iter = QtWidgets.QLabel(self.centralwidget)
        self.lbl_iter.setObjectName("lbl_iter")
        self.gridLayout.addWidget(self.lbl_iter, 8, 3, 1, 1)
        self.slider_iter = QtWidgets.QSlider(self.centralwidget)
        self.slider_iter.setMinimum(1)
        self.slider_iter.setMaximum(10)
        self.slider_iter.setOrientation(QtCore.Qt.Horizontal)
        self.slider_iter.setObjectName("slider_iter")
        self.gridLayout.addWidget(self.slider_iter, 8, 4, 1, 1)
        self.lbl_l = QtWidgets.QLabel(self.centralwidget)
        self.lbl_l.setObjectName("lbl_l")
        self.gridLayout.addWidget(self.lbl_l, 8, 5, 1, 1)
        self.slider_l = QtWidgets.QSlider(self.centralwidget)
        self.slider_l.setMinimum(10)
        self.slider_l.setMaximum(100)
        self.slider_l.setProperty("value", 20)
        self.slider_l.setOrientation(QtCore.Qt.Horizontal)
        self.slider_l.setObjectName("slider_l")
        self.gridLayout.addWidget(self.slider_l, 8, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 7, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Задание 7"))
        self.lbl_angle.setText(_translate("MainWindow", "Угол"))
        self.btn.setText(_translate("MainWindow", "Загрузить из файла"))
        self.lbl_info.setText(_translate("MainWindow", "Угол: 0    Итерация: 0   Длина: 20"))
        self.lbl_teo3.setText(_translate("MainWindow", "Теорема 3"))
        self.lbl_teo2.setText(_translate("MainWindow", "Теорема 2"))
        self.lbl_teo1.setText(_translate("MainWindow", "Теорема 1"))
        self.lbl_aks.setText(_translate("MainWindow", "Аксиома"))
        self.lbl_iter.setText(_translate("MainWindow", "Итерация"))
        self.lbl_l.setText(_translate("MainWindow", "Длина"))
