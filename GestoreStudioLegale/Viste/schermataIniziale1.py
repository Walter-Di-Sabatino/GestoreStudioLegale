# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schermataIniziale1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(486, 392)
        Form.setStyleSheet("\n"
"background: rgb(255, 240, 186);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 30, 221, 41))
        self.label.setStyleSheet("font: italic 30pt \"Baskerville\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 181, 32))
        self.pushButton.setStyleSheet("\n"
"border-width: 2px;\n"
"\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 10em; \n"
"background-color: rgb(255, 255, 229);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 210, 181, 32))
        self.pushButton_2.setStyleSheet("\n"
"border-width: 2px;\n"
"\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 10em; \n"
"background-color: rgb(255, 255, 229);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 270, 181, 31))
        self.pushButton_3.setStyleSheet("\n"
"border-width: 2px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 10em; \n"
"background-color: rgb(255, 255, 229);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 251, 16))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/istockphoto-1077097764-1024x1024.jpeg);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(370, 20, 101, 51))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/giustizia-legalita.jpg);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/giustizia-legalita.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "STUDIO LEGALE"))
        self.pushButton.setText(_translate("Form", "CLIENTE"))
        self.pushButton_2.setText(_translate("Form", "AVVOCATO"))
        self.pushButton_3.setText(_translate("Form", "AMMINISTRATORE"))
        self.label_2.setText(_translate("Form", "SELEZIONARE TIPOLOGIA UTENTE :"))
import Immagine_rc
