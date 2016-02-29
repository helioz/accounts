# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon Feb 29 18:48:10 2016
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
        self.addService = QtGui.QFrame(self.centralwidget)
        self.addService.setGeometry(QtCore.QRect(40, 10, 731, 531))
        self.addService.setFrameShape(QtGui.QFrame.StyledPanel)
        self.addService.setFrameShadow(QtGui.QFrame.Raised)
        self.addService.setObjectName(_fromUtf8("addService"))
        self.label = QtGui.QLabel(self.addService)
        self.label.setGeometry(QtCore.QRect(70, 160, 62, 23))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.addService)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 62, 23))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.addService)
        self.label_3.setGeometry(QtCore.QRect(70, 330, 62, 23))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditName = QtGui.QLineEdit(self.addService)
        self.lineEditName.setGeometry(QtCore.QRect(230, 150, 113, 35))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.lineEditPhone = QtGui.QLineEdit(self.addService)
        self.lineEditPhone.setGeometry(QtCore.QRect(230, 220, 113, 35))
        self.lineEditPhone.setObjectName(_fromUtf8("lineEditPhone"))
        self.pushButtonSubmit = QtGui.QPushButton(self.addService)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(500, 370, 151, 81))
        self.pushButtonSubmit.setObjectName(_fromUtf8("pushButtonSubmit"))
        self.textEditNotes = QtGui.QTextEdit(self.addService)
        self.textEditNotes.setGeometry(QtCore.QRect(230, 320, 104, 75))
        self.textEditNotes.setObjectName(_fromUtf8("textEditNotes"))
        self.Title = QtGui.QLabel(self.addService)
        self.Title.setGeometry(QtCore.QRect(181, 50, 241, 61))
        self.Title.setObjectName(_fromUtf8("Title"))
        self.pushButtonBack = QtGui.QPushButton(self.addService)
        self.pushButtonBack.setGeometry(QtCore.QRect(80, 450, 92, 33))
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Name", None))
        self.label_2.setText(_translate("MainWindow", "Phone No:", None))
        self.label_3.setText(_translate("MainWindow", "Notes", None))
        self.pushButtonSubmit.setText(_translate("MainWindow", "PushButton", None))
        self.Title.setText(_translate("MainWindow", "Create Service", None))
        self.pushButtonBack.setText(_translate("MainWindow", "Back", None))

