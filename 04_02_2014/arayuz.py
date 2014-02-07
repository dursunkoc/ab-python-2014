#-*- encoding: utf-8 -*- 
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class Pencere(QtGui.QWidget):
    def __init__(self):
        super(Pencere, self).__init__()

        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('Pencere')
        self.setToolTip("Pencere")

        self.button = QtGui.QPushButton('Cikis', self)
        self.button.setToolTip("Bu butona basinca uygulamadan çıkar")
        self.button.move(30, 30)

        self.button.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec_())

