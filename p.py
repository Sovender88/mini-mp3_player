# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 87)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 50, 181, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Button_open = QtWidgets.QPushButton(Form)
        self.Button_open.setGeometry(QtCore.QRect(8, 21, 31, 24))
        self.Button_open.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("картинки/plus.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_open.setIcon(icon)
        self.Button_open.setObjectName("Button_open")
        self.Button_stop = QtWidgets.QPushButton(Form)
        self.Button_stop.setGeometry(QtCore.QRect(100, 20, 28, 24))
        self.Button_stop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("картинки/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_stop.setIcon(icon1)
        self.Button_stop.setObjectName("Button_stop")
        self.Button_next = QtWidgets.QPushButton(Form)
        self.Button_next.setGeometry(QtCore.QRect(130, 20, 28, 24))
        self.Button_next.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("картинки/next.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_next.setIcon(icon2)
        self.Button_next.setObjectName("Button_next")
        self.Button_shuffle = QtWidgets.QPushButton(Form)
        self.Button_shuffle.setGeometry(QtCore.QRect(160, 20, 31, 24))
        self.Button_shuffle.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("картинки/mix.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_shuffle.setIcon(icon3)
        self.Button_shuffle.setObjectName("Button_shuffle")
        self.Button_play = QtWidgets.QPushButton(Form)
        self.Button_play.setGeometry(QtCore.QRect(70, 20, 28, 24))
        self.Button_play.setText("‣")
        self.Button_play.setObjectName("Button_play")
        self.Button_prev = QtWidgets.QPushButton(Form)
        self.Button_prev.setGeometry(QtCore.QRect(40, 20, 28, 24))
        self.Button_prev.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("картинки/previous.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_prev.setIcon(icon5)
        self.Button_prev.setObjectName("Button_prev")
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(200, 20, 22, 51))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

