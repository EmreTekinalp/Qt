# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GitHub\Qt\src\python\list_widget\list_widget.ui'
#
# Created: Sat Mar 25 18:44:37 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 321)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.createBtn = QtGui.QPushButton(self.centralwidget)
        self.createBtn.setObjectName("createBtn")
        self.verticalLayout.addWidget(self.createBtn)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.bakeBtn = QtGui.QPushButton(self.centralwidget)
        self.bakeBtn.setObjectName("bakeBtn")
        self.verticalLayout.addWidget(self.bakeBtn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.createBtn.setText(QtGui.QApplication.translate("MainWindow", "create", None, QtGui.QApplication.UnicodeUTF8))
        self.bakeBtn.setText(QtGui.QApplication.translate("MainWindow", "bake", None, QtGui.QApplication.UnicodeUTF8))

