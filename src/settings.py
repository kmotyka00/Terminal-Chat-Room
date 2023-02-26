import socket 

HEADER = 64 # first message to the server will have 64 bytes and tell the length of the message 
PORT = 5065
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"