#-*- encoding: utf-8 -*-
import socket
import select

class ChatServer:
    def __init__(self, host="localhost", port=8080):
        self.host = host
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.descriptors = [self.server_socket]
        self.allowed_hosts = {}

        print "Chat chat started on {0}:{1}".format(self.host, self.port)

    def run(self):
        while True:
            # Await an event on a readable socket descriptor
            (sread, swrite, sexc) = select.select( self.descriptors, [], [] )

            for sock in sread:

                if sock == self.server_socket:
                    self.accept_new_connection()
                else:
                    message = sock.recv(1024)
                    if message == '':
                        host, port = sock.getpeername()
                        str = "SERVER Client left {0}:{1}".format(host, port)
                        self.broadcast_string(str, sock)
                        sock.close()
                        self.descriptors.remove(sock)
                    else:
                        host, port = sock.getpeername()
                        splitted_message = message.split(" ", 1)
                        if splitted_message[0] == "USERNAME":
                            username = splitted_message[1]
                            self.allowed_hosts["%s:%s" % (host,port)] = username
                            message_to_send = 'SERVER %s joined to room' % (username)
                            self.broadcast_string(message_to_send, sock)
                        else:
                            username = self.allowed_hosts["%s:%s" % (host, port)]
                            self.broadcast_string("%s> %s" % (username, message), sock)



    def accept_new_connection(self):
        new_socket, (remhost, remport) = self.server_socket.accept()
        self.descriptors.append(new_socket)

        new_socket.send("SERVER You're connected to the AB2014 chatserver")
        #message = 'SERVER Client joined %s:%s\n' % (remhost, remport)
        #self.broadcast_string(message, new_socket)

    def broadcast_string(self, message, omit_socket):
        for socket in self.descriptors:
            if socket != self.server_socket and socket != omit_socket:
                socket.send(message)

        print message

if __name__ == "__main__":
    server = ChatServer(host="192.168.1.24")
    server.run()