'''
Bryan Baraoidan
mudclient.py
This file defines the client side of the mud client server
'''
import sys
from socketwrapper import SocketWrapper

def main():
    client_socket = SocketWrapper('<<EOC')

    try:
        client_socket.host_name = sys.argv[1]
        client_socket.port_number = int(sys.argv[2])
    except:
        print "Usage: mudclient.py HOSTNAME PORT"
        sys.exit(1)

    client_socket.buffer_size = 4096
    #servers bind clients connect
    client_socket.connectToServer()
    #recieve and print intro message
    print client_socket.recieveData()

    while(1):
        message = raw_input("Enter Command: ")
        message += '<<EOC'
        client_socket.sendMessage(message)
        data = client_socket.recieveData()
        if message.lower() == "quit<<eoc": 
            break
        print data

    client_socket.closeConnection()

if __name__ == "__main__":
    main()
