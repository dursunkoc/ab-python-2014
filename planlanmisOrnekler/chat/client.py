#-*- encoding: utf-8 -*-

from PyQt4 import QtCore
import socket

class Client(QtCore.QThread):
    def __init__(self, host, port, buffer_size=1024):
        QtCore.QThread.__init__(self)
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
 
    def send(self, data):
        self.client_socket.send(data)
 
    def run(self):
        while True:
            data = self.client_socket.recv(self.buffer_size)
            self.process_data(data)
			
    def process_data(self, data):
        splitted_data = data.split(" ", 1)
        if splitted_data[0] == "SERVER":
            self.emit(QtCore.SIGNAL('message_received_from_server'), splitted_data[1])
        else:
            self.emit(QtCore.SIGNAL('message_received'), data)

    def send_username(self, username):
        data = "USERNAME " + username
        self.client_socket.send(data)
