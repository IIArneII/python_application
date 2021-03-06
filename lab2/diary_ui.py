# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diary.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class DiaryUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1003, 586)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.name_line = QtWidgets.QLineEdit(Form)
        self.name_line.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.name_line.setFont(font)
        self.name_line.setObjectName("name_line")
        self.gridLayout.addWidget(self.name_line, 0, 1, 1, 1)
        self.add_btn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.add_btn.setFont(font)
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 0, 2, 1, 1)
        self.del_btn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.del_btn.setFont(font)
        self.del_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.del_btn.setObjectName("del_btn")
        self.gridLayout.addWidget(self.del_btn, 0, 3, 1, 1)
        self.time_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.gridLayout.addWidget(self.time_label, 1, 0, 1, 1)
        self.time_line = QtWidgets.QTimeEdit(Form)
        self.time_line.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.time_line.setFont(font)
        self.time_line.setObjectName("time_line")
        self.gridLayout.addWidget(self.time_line, 1, 1, 1, 1)
        self.note_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.note_label.setFont(font)
        self.note_label.setScaledContents(False)
        self.note_label.setAlignment(QtCore.Qt.AlignCenter)
        self.note_label.setObjectName("note_label")
        self.gridLayout.addWidget(self.note_label, 2, 0, 1, 2)
        self.note_edit = QtWidgets.QPlainTextEdit(Form)
        self.note_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.note_edit.setFont(font)
        self.note_edit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.note_edit.setObjectName("note_edit")
        self.gridLayout.addWidget(self.note_edit, 3, 0, 1, 2)
        self.calendar = QtWidgets.QCalendarWidget(Form)
        self.calendar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.calendar.setFont(font)
        self.calendar.setObjectName("calendar")
        self.gridLayout.addWidget(self.calendar, 4, 0, 1, 2)
        self.event_list = QtWidgets.QListWidget(Form)
        self.event_list.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.event_list.setFont(font)
        self.event_list.setObjectName("event_list")
        self.gridLayout.addWidget(self.event_list, 1, 2, 4, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_label.setText(_translate("Form", "????????????????"))
        self.add_btn.setText(_translate("Form", "+"))
        self.del_btn.setText(_translate("Form", "??????????????"))
        self.time_label.setText(_translate("Form", "??????????"))
        self.note_label.setText(_translate("Form", "????????????????????"))
