#-*- encoding: utf-8 -*-

from PyQt4 import QtGui , QtCore
from chat.client import Client
import sys



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_client()

    def init_client(self):
        roomLabel = QtGui.QLabel('AB2014')

        self.browser = QtGui.QTextBrowser()

        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setMaximumSize(QtCore.QSize(500,60))
        self.connect(self.textEdit, QtCore.SIGNAL("returnPressed()"),self.callback)

        self.sendButton = QtGui.QPushButton('Send')
        self.sendButton.setMaximumSize(QtCore.QSize(500,60))
        self.sendButton.clicked.connect(self.callback)

        layoutINlayout = QtGui.QHBoxLayout()
        layoutINlayout.addWidget(self.textEdit)
        layoutINlayout.addWidget(self.sendButton)


        widget = QtGui.QWidget()
        self.setCentralWidget(widget)

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.browser)

        mainwindow = QtGui.QVBoxLayout()
        mainwindow.addLayout (self.layout )
        mainwindow.addLayout (layoutINlayout )

        widget.setLayout(mainwindow)

        self.setWindowTitle("AB2014 Chat Client")
        self.setGeometry(200, 200, 600, 600)
        self.show()

        self.get_connection_parameters()
        self.client = Client(self.hostname, self.port)

        self.client.start()
        QtCore.QObject.connect(self.client, QtCore.SIGNAL('message_received'), self.show_message)
        QtCore.QObject.connect(self.client, QtCore.SIGNAL('message_received_from_server'), self.show_server_message)

        self.client.send_username(str(self.username))
        self.statusBar().showMessage('Connected to {0}:{1} as {2}'.format(self.hostname, self.port, self.username))


    def get_connection_parameters(self):
        text, username_ok = QtGui.QInputDialog.getText(self, 'username', 'Enter user name:')
        if username_ok:
            self.username = text
        else:
            QtCore.QCoreApplication.instance().quit

        text, hostname_ok = QtGui.QInputDialog.getText(self, 'Hostname', 'Enter host name:')
        if hostname_ok:
            self.hostname = text
        else:
            QtCore.QCoreApplication.instance().quit

        text, port_ok = QtGui.QInputDialog.getText(self, 'Port', 'Enter port number:')
        if port_ok:
            self.port = int(text)
        else:
            QtCore.QCoreApplication.instance().quit

        if self.username == None or self.hostname == None or self.port == None:
            QtCore.QCoreApplication.instance().quit


    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def callback(self, event):
        message = unicode(self.textEdit.toPlainText())
        self.client.send(message)

    def show_message(self, data):
        self.browser.insertHtml(QtCore.QString("<span style=\" color:#00ff00;\">%1</span><br>").arg(data))

    def show_server_message(self, data):
        self.browser.insertHtml(QtCore.QString("<span style=\" color:#ff0000;\">%1</span><br>").arg(data))

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    app.setStyle('chat')


    window = MainWindow()
    sys.exit(app.exec_())
