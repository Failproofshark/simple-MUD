'''
Bryan Baraoidan
socketwrapper.py
A simple wrapper class for the python socket class 
'''
import socket

class SocketWrapper:
    def __init__(self, end_marker=None, socketPrototype=None):
        if socketPrototype == None:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.socket= socketPrototype
        self.queue_size = 1
        self.host_name = ''
        self.port_number = 0
        self.buffer_size = 1024
        #Used to signal the end of a message
        self.end_marker = end_marker

    def __del__(self):
        self.closeConnection()

    def startListening(self):
        self.socket.bind((self.host_name, self.port_number))
        self.socket.listen(self.queue_size)

    def awaitConnection(self):
        socket, address = self.socket.accept()
        print "connection at ", address
        return socket

    def connectToServer(self):
        self.socket.connect((self.host_name, self.port_number))

    #utilizes an end of marker to denote the end of a message
    def recieveData(self):
        all_data = []
        while True:
            data = self.socket.recv(self.buffer_size)
            all_data.append(data)
            if self.end_marker in data: break
        command = ''.join(all_data)
        #just return the message part of the string
        return command[:command.find(self.end_marker)]

    def sendMessage(self, message):
        self.socket.sendall(message)

    def closeConnection(self):
        self.socket.close()
