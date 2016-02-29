# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon Feb 29 21:48:13 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 10, 731, 521))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.createClient = QtGui.QWidget()
        self.createClient.setObjectName(_fromUtf8("createClient"))
        self.label = QtGui.QLabel(self.createClient)
        self.label.setGeometry(QtCore.QRect(221, 30, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.createClient)
        self.label_2.setGeometry(QtCore.QRect(21, 160, 111, 23))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.createClient)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 62, 23))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.createClient)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 62, 23))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButtonNext = QtGui.QPushButton(self.createClient)
        self.pushButtonNext.setGeometry(QtCore.QRect(520, 330, 141, 71))
        self.pushButtonNext.setObjectName(_fromUtf8("pushButtonNext"))
        self.lineEditName = QtGui.QLineEdit(self.createClient)
        self.lineEditName.setGeometry(QtCore.QRect(210, 150, 241, 35))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.textEditInfo = QtGui.QTextEdit(self.createClient)
        self.textEditInfo.setGeometry(QtCore.QRect(210, 330, 241, 75))
        self.textEditInfo.setObjectName(_fromUtf8("textEditInfo"))
        self.lineEditPhone = QtGui.QLineEdit(self.createClient)
        self.lineEditPhone.setGeometry(QtCore.QRect(210, 240, 241, 35))
        self.lineEditPhone.setObjectName(_fromUtf8("lineEditPhone"))
        self.pushButtonBackNewClient = QtGui.QPushButton(self.createClient)
        self.pushButtonBackNewClient.setGeometry(QtCore.QRect(50, 450, 91, 21))
        self.pushButtonBackNewClient.setObjectName(_fromUtf8("pushButtonBackNewClient"))
        self.stackedWidget.addWidget(self.createClient)
        self.confirmClient = QtGui.QWidget()
        self.confirmClient.setObjectName(_fromUtf8("confirmClient"))
        self.label_5 = QtGui.QLabel(self.confirmClient)
        self.label_5.setGeometry(QtCore.QRect(260, 60, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButtonConfirm = QtGui.QPushButton(self.confirmClient)
        self.pushButtonConfirm.setGeometry(QtCore.QRect(510, 380, 92, 33))
        self.pushButtonConfirm.setObjectName(_fromUtf8("pushButtonConfirm"))
        self.pushButtonBack = QtGui.QPushButton(self.confirmClient)
        self.pushButtonBack.setGeometry(QtCore.QRect(100, 380, 92, 33))
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))
        self.textBrowserConfirmClientInfo = QtGui.QTextBrowser(self.confirmClient)
        self.textBrowserConfirmClientInfo.setGeometry(QtCore.QRect(185, 161, 411, 121))
        self.textBrowserConfirmClientInfo.setObjectName(_fromUtf8("textBrowserConfirmClientInfo"))
        self.stackedWidget.addWidget(self.confirmClient)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Add new Client", None))
        self.label_2.setText(_translate("MainWindow", "Name", None))
        self.label_3.setText(_translate("MainWindow", "Phone No.", None))
        self.label_4.setText(_translate("MainWindow", "Info", None))
        self.pushButtonNext.setText(_translate("MainWindow", "Submit", None))
        self.pushButtonBackNewClient.setText(_translate("MainWindow", "Back", None))
        self.label_5.setText(_translate("MainWindow", "Are you sure?", None))
        self.pushButtonConfirm.setText(_translate("MainWindow", "Yes.", None))
        self.pushButtonBack.setText(_translate("MainWindow", "Back", None))

