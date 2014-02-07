from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import sys

class Tarayici(QWidget):
     def __init__(self):
         super(Tarayici, self).__init__()

         self.webview = QWebView(self)
         self.webview.load(QUrl(sys.argv[1]))
         self.setWindowTitle("Tarayici")
         self.resize(700,700)   
         self.show()

if __name__ == "__main__":
     app = QApplication(sys.argv)
     tarayici = Tarayici()
     sys.exit(app.exec_())
