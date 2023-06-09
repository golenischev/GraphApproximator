# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutprog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 488)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "О программе - Аппроксимация графиков"))
        self.label.setText(_translate("Dialog", "Министерство науки и высшего образования Российской Федерации\n"
"ФГАОУ ВО \"Южно-Уральский Государственный Университет (НИУ)\"\n"
"Институт естественных и точных наук\n"
"Кафедра \"Физика наноразмерных систем\"\n"
"\n"
"\n"
"Программа \"Аппроксимация графиков\"\n"
"Версия 1.0\n"
"\n"
"\n"
"Разработал: Голенищев А. Б.\n"
"\n"
"\n"
"Челябинск 2023\n"
"\n"
"Лицензия GNU GPL 3.0"))
