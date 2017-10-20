# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audioFlashcard.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 516)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(40, 40, 40);")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setObjectName("stackedWidget")
        self.title_page = QtWidgets.QWidget()
        self.title_page.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_page.setObjectName("title_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.title_page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nameLab = QtWidgets.QLabel(self.title_page)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.nameLab.setFont(font)
        self.nameLab.setObjectName("nameLab")
        self.horizontalLayout_4.addWidget(self.nameLab)
        self.nameLed = QtWidgets.QLineEdit(self.title_page)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.nameLed.setFont(font)
        self.nameLed.setFrame(False)
        self.nameLed.setObjectName("nameLed")
        self.horizontalLayout_4.addWidget(self.nameLed)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.titleLab = QtWidgets.QLabel(self.title_page)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titleLab.setFont(font)
        self.titleLab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLab.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLab.setObjectName("titleLab")
        self.verticalLayout.addWidget(self.titleLab)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 20, 10, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.englishLab = QtWidgets.QLabel(self.title_page)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        self.englishLab.setFont(font)
        self.englishLab.setStyleSheet("color: rgb(183, 10, 70);")
        self.englishLab.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.englishLab.setAlignment(QtCore.Qt.AlignCenter)
        self.englishLab.setObjectName("englishLab")
        self.horizontalLayout_2.addWidget(self.englishLab)
        self.japaneseLab = QtWidgets.QLabel(self.title_page)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        self.japaneseLab.setFont(font)
        self.japaneseLab.setStyleSheet("color: rgb(183, 10, 70);")
        self.japaneseLab.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.japaneseLab.setAlignment(QtCore.Qt.AlignCenter)
        self.japaneseLab.setObjectName("japaneseLab")
        self.horizontalLayout_2.addWidget(self.japaneseLab)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 165, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.title_page)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.previousBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousBtn.sizePolicy().hasHeightForWidth())
        self.previousBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.previousBtn.setFont(font)
        self.previousBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.previousBtn.setStyleSheet("QPushButton{border: none;}\n"
"QPushButton:hover{\n"
"border: none;\n"
"color: rgb(255, 60, 60);\n"
"}\n"
"QPushButton:pressed{\n"
"border: none;\n"
"color: rgb(255, 60, 60);\n"
"font-size: 16pt\n"
"}")
        self.previousBtn.setObjectName("previousBtn")
        self.horizontalLayout_3.addWidget(self.previousBtn)
        self.pageLab = QtWidgets.QLabel(self.centralwidget)
        self.pageLab.setStyleSheet("color: rgb(255, 204, 0);")
        self.pageLab.setObjectName("pageLab")
        self.horizontalLayout_3.addWidget(self.pageLab)
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nextBtn.setFont(font)
        self.nextBtn.setStyleSheet("QPushButton{border: none;}\n"
"QPushButton:hover{\n"
"border: none;\n"
"color: rgb(60, 255, 60);\n"
"}\n"
"QPushButton:pressed{\n"
"border: none;\n"
"color: rgb(60, 255, 60);\n"
"font-size: 16pt\n"
"}")
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout_3.addWidget(self.nextBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameLab.setText(_translate("MainWindow", "Name:"))
        self.nameLed.setPlaceholderText(_translate("MainWindow", "Please specify your name"))
        self.titleLab.setText(_translate("MainWindow", "My Vocabulary Book"))
        self.englishLab.setText(_translate("MainWindow", "english"))
        self.japaneseLab.setText(_translate("MainWindow", "japanese"))
        self.previousBtn.setText(_translate("MainWindow", "<<"))
        self.pageLab.setText(_translate("MainWindow", "0"))
        self.nextBtn.setText(_translate("MainWindow", ">>"))
        self.actionSave.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setText(_translate("MainWindow", "Save"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionNew.setText(_translate("MainWindow", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

