# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'styl.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(719, 547)
        self.rzut = QtWidgets.QPushButton(Form)
        self.rzut.setGeometry(QtCore.QRect(270, 60, 181, 61))
        self.rzut.setObjectName("rzut")
        self.kosc2 = QtWidgets.QLabel(Form)
        self.kosc2.setGeometry(QtCore.QRect(150, 170, 121, 101))
        self.kosc2.setText("")
        self.kosc2.setPixmap(QtGui.QPixmap("pliki/question.jpg"))
        self.kosc2.setScaledContents(True)
        self.kosc2.setObjectName("kosc2")
        self.kosc1 = QtWidgets.QLabel(Form)
        self.kosc1.setGeometry(QtCore.QRect(20, 170, 121, 101))
        self.kosc1.setText("")
        self.kosc1.setPixmap(QtGui.QPixmap("pliki/question.jpg"))
        self.kosc1.setScaledContents(True)
        self.kosc1.setObjectName("kosc1")
        self.kosc3 = QtWidgets.QLabel(Form)
        self.kosc3.setGeometry(QtCore.QRect(290, 170, 121, 101))
        self.kosc3.setText("")
        self.kosc3.setPixmap(QtGui.QPixmap("pliki/question.jpg"))
        self.kosc3.setScaledContents(True)
        self.kosc3.setObjectName("kosc3")
        self.kosc4 = QtWidgets.QLabel(Form)
        self.kosc4.setGeometry(QtCore.QRect(430, 170, 121, 101))
        self.kosc4.setText("")
        self.kosc4.setPixmap(QtGui.QPixmap("pliki/question.jpg"))
        self.kosc4.setScaledContents(True)
        self.kosc4.setObjectName("kosc4")
        self.kosc5 = QtWidgets.QLabel(Form)
        self.kosc5.setGeometry(QtCore.QRect(580, 170, 121, 101))
        self.kosc5.setText("")
        self.kosc5.setPixmap(QtGui.QPixmap("pliki/question.jpg"))
        self.kosc5.setScaledContents(True)
        self.kosc5.setObjectName("kosc5")
        self.wynik_tego_losowania = QtWidgets.QLabel(Form)
        self.wynik_tego_losowania.setGeometry(QtCore.QRect(300, 310, 141, 41))
        self.wynik_tego_losowania.setObjectName("wynik_tego_losowania")
        self.wynik_gry = QtWidgets.QLabel(Form)
        self.wynik_gry.setGeometry(QtCore.QRect(330, 360, 161, 41))
        self.wynik_gry.setObjectName("wynik_gry")
        self.reset = QtWidgets.QPushButton(Form)
        self.reset.setGeometry(QtCore.QRect(280, 420, 171, 71))
        self.reset.setObjectName("reset")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rzut.setText(_translate("Form", "rzuć koścmi"))
        self.wynik_tego_losowania.setText(_translate("Form", "Wynik tego losowania: 0"))
        self.wynik_gry.setText(_translate("Form", "Wynik gry: 0"))
        self.reset.setText(_translate("Form", "RESETUJ WYNIK"))
