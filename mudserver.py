'''
Bryan Baraoidan
mudserver.py
This defines the server half of the mud client server
'''

import socket, thread, sys

from playercharacter import PlayerCharacter
from mudactions import MudActions
from mudmap import MudMap
from socketwrapper import SocketWrapper

#The world should be global to all players in order for them to change
#it and make their changes visible to others
world = MudMap()

def main():
    '''
    Once the socket is bound the client is handled in another thread to
    allow for asynchronous input
    '''
    print "Press ctrl-c to stop server..."
    listener_socket = SocketWrapper()
    #Serving local clients only for efficiancy purposes
    try:
        listener_socket.port_number = int(sys.argv[1])
    except:
        print "Usage: mudserver.py PORT"
        sys.exit(1)   

    #change hostname to inet address of computer the server is run on
    listener_socket.host_name = ''
    listener_socket.queue_size = 2
    listener_socket.buffer_size = 4096

    listener_socket.startListening()

    while 1:
        communication_socket = \
            SocketWrapper("<<EOC", listener_socket.awaitConnection())
        thread.start_new_thread(threadHandler, (communication_socket,))
        
    listener_socket.closeConnection()

def threadHandler(communication_socket):
    '''
    Once a request comes in it must be handled in a separate thread,
    otherwise one client will be waiting for another to send a message
    or receive a reply from the server
    '''
    actions = MudActions()
    player = PlayerCharacter()
    intro = '''The night is late and you're in your room coding on
your Commodore 64 with your sunglasses just like any other cool coder
would. Suddenly a blinding light shines through your blackout curtains
and a gut wrenching feeling grips you as you suddenly begin to fade
away then black out...\n\nWhen you come to you find yourself somewhere
deep in space...<<EOC'''
    communication_socket.sendMessage(intro)
    while True:
        command = communication_socket.recieveData()
        reply = ""
        if command.lower() == "quit": break
        else: reply = actions.performAction(command, player, world)
        reply += "<<EOC"
        communication_socket.sendMessage(reply) 

    #send connection termination message
    communication_socket.sendMessage("Terminate Connection<<EOC") 
    communication_socket.closeConnection()
    print "socket successfully closed"

if __name__ == "__main__":
    main()
