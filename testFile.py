import database.dbManager as dB

from PyQt4 import QtCore
from PyQt4 import QtGui
import ux.mainWindow as window

import sys

dbObj = dB.DatabaseLayer(dB.dbName)

class MainForm(QtGui.QMainWindow, window.Ui_MainWindow):
    widgetDict = {'createClient':0,'confirmClient':1}
    def __init__(self, parent = None):
        super(MainForm,self).__init__(parent)
        #self.ui = 
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(self.widgetDict['createClient'])
        QtCore.QObject.connect(self.pushButtonNext,QtCore.SIGNAL("clicked()"),self.buttonclickSubmit)
        QtCore.QObject.connect(self.pushButtonBack, QtCore.SIGNAL("clicked()"),self.buttonclickBack)
    def buttonclickSubmit(self):
        name = self.lineEditName.text()
        phoneNumber = self.lineEditPhone.text()
        notes = self.textEditInfo.toPlainText()
        self.stackedWidget.setCurrentIndex(self.widgetDict['confirmClient'])
        self.textBrowserConfirmClientInfo.setText("Name:\tPhone:\tNotes\n{}\t{}\t{}".format(name,phoneNumber,notes))
        #dbObj.addService(name,phoneNumber,notes)  #Add after completing ui

        
    def buttonclickBack(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()

if __name__=="__main__":
    main()    
