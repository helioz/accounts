import database.dbManager as dB

from PyQt4 import QtCore
from PyQt4 import QtGui
import ux.mainWindow as window

import sys

dbObj = dB.DatabaseLayer(dB.dbName)

class MainForm(QtGui.QMainWindow, window.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainForm,self).__init__(parent)
        #self.ui = 
        self.setupUi(self)
        QtCore.QObject.connect(self.pushButtonSubmit,QtCore.SIGNAL("clicked()"),self.buttonclickSubmit)
    def buttonclickSubmit(self):
        name = self.lineEditName.text()
        phoneNumber = self.lineEditPhone.text()
        notes = self.textEditNotes.toPlainText()
        #dbObj.addService(name,phoneNumber,notes)  #Add after completing ui
        self.addService.hide()

        
def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()

if __name__=="__main__":
    main()    
