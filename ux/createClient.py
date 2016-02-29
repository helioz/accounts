# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createClient.ui'
#
# Created: Sun Feb 28 22:11:33 2016
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
        font = QtGui.QFont()
        font.setPointSize(21)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEditNotes = QtGui.QTextEdit(self.centralwidget)
        self.textEditNotes.setGeometry(QtCore.QRect(180, 300, 271, 75))
        self.textEditNotes.setObjectName(_fromUtf8("textEditNotes"))
        self.lineEditName = QtGui.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(180, 150, 271, 35))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.lineEditPhone = QtGui.QLineEdit(self.centralwidget)
        self.lineEditPhone.setGeometry(QtCore.QRect(180, 220, 271, 31))
        self.lineEditPhone.setObjectName(_fromUtf8("lineEditPhone"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(251, 50, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 62, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 62, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 320, 62, 23))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.addClientButton = QtGui.QPushButton(self.centralwidget)
        self.addClientButton.setGeometry(QtCore.QRect(340, 410, 151, 51))
        self.addClientButton.setObjectName(_fromUtf8("addClientButton"))
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(80, 460, 92, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 48))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionBack = QtGui.QAction(MainWindow)
        self.actionBack.setObjectName(_fromUtf8("actionBack"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuMenu.addAction(self.actionBack)
        self.menuMenu.addAction(self.actionSave)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Create a new Client", None))
        self.label_2.setText(_translate("MainWindow", "Name:", None))
        self.label_3.setText(_translate("MainWindow", "Phone:", None))
        self.label_4.setText(_translate("MainWindow", "Info:", None))
        self.addClientButton.setText(_translate("MainWindow", "Add Client", None))
        self.backButton.setText(_translate("MainWindow", "<- Back", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.actionBack.setText(_translate("MainWindow", "Back", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))

